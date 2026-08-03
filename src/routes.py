from dataclasses import asdict
from typing import List

from fastapi import APIRouter, HTTPException, status

from models import Expense
from schemas import (
    ExpenseCreate,
    ExpenseResponse,
    TotalResponse,
    CategoryTotalResponse,
)
from storage import (
    load_expenses,
    save_expenses,
    generate_next_id,
)
from  utils import (
    filter_expenses_by_category,
    calculate_total_expenses,
    calculate_category_total,
)

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.post(
    "",
    response_model=ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_expense(expense: ExpenseCreate):
    expenses = load_expenses()

    new_expense = Expense(
        id=generate_next_id(expenses),
        title=expense.title,
        amount=expense.amount,
        category=expense.category.value,
        date=expense.date,
    )

    expenses.append(new_expense)
    save_expenses(expenses)

    return asdict(new_expense)


@router.get(
    "",
    response_model=List[ExpenseResponse],
)
def get_all_expenses():
    expenses = load_expenses()
    return [asdict(expense) for expense in expenses]


@router.get(
    "/category/{category}",
    response_model=List[ExpenseResponse],
)
def get_expenses_by_category(category: str):
    expenses = load_expenses()

    filtered = filter_expenses_by_category(
        expenses,
        category,
    )

    return [asdict(expense) for expense in filtered]


@router.get(
    "/total",
    response_model=TotalResponse,
)
def get_total_expenses():
    expenses = load_expenses()

    total = calculate_total_expenses(expenses)

    return {
        "total": total
    }


@router.get(
    "/total/{category}",
    response_model=CategoryTotalResponse,
)
def get_total_by_category(category: str):
    expenses = load_expenses()

    total = calculate_category_total(
        expenses,
        category,
    )

    return {
        "category": category,
        "total": total,
    }


@router.delete(
    "/{expense_id}",
    status_code=status.HTTP_200_OK,
)
def delete_expense(expense_id: int):
    expenses = load_expenses()

    expense = next(
        (
            expense
            for expense in expenses
            if expense.id == expense_id
        ),
        None,
    )

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found",
        )

    expenses.remove(expense)
    save_expenses(expenses)

    return {
        "message": "Expense deleted successfully"
    }