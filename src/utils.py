from typing import List

from models import Expense


def filter_expenses_by_category(
    expenses: List[Expense],
    category: str,
) -> List[Expense]:
    """
    Return all expenses matching the given category.
    """
    return [
        expense
        for expense in expenses
        if expense.category.lower() == category.lower()
    ]


def calculate_total_expenses(expenses: List[Expense]) -> float:
    """
    Calculate the total amount of all expenses.
    """
    return round(
        sum(expense.amount for expense in expenses),
        2
    )


def calculate_category_total(
    expenses: List[Expense],
    category: str,
) -> float:
    """
    Calculate the total amount for a specific category.
    """
    total = sum(
        expense.amount
        for expense in expenses
        if expense.category.lower() == category.lower()
    )

    return round(total, 2)