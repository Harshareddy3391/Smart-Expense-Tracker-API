import json
from pathlib import Path
from typing import List

from  models import Expense

# Path to expenses.json in the project root
DATA_FILE = Path(__file__).resolve().parent.parent / "expenses.json"


def load_expenses() -> List[Expense]:
    """
    Load all expenses from the JSON file.
    """
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return []

    expenses = []

    for item in data:
        expenses.append(
            Expense(
                id=item["id"],
                title=item["title"],
                amount=item["amount"],
                category=item["category"],
                date=item["date"],
            )
        )

    return expenses


def save_expenses(expenses: List[Expense]) -> None:
    """
    Save all expenses to the JSON file.
    """
    data = []

    for expense in expenses:
        data.append(
            {
                "id": expense.id,
                "title": expense.title,
                "amount": expense.amount,
                "category": expense.category,
                "date": str(expense.date),
            }
        )

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def generate_next_id(expenses: List[Expense]) -> int:
    """
    Generate the next expense ID.
    """
    if not expenses:
        return 1

    return max(expense.id for expense in expenses) + 1