from dataclasses import dataclass
from datetime import date


@dataclass
class Expense:
    """
    Represents a single expense record.
    """

    id: int
    title: str
    amount: float
    category: str
    date: date