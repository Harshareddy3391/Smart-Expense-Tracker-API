from datetime import date
from enum import Enum

from pydantic import BaseModel, Field


class Category(str, Enum):
    FOOD = "Food"
    TRAVEL = "Travel"
    SHOPPING = "Shopping"
    BILLS = "Bills"
    ENTERTAINMENT = "Entertainment"
    HEALTH = "Health"
    EDUCATION = "Education"
    OTHER = "Other"


class ExpenseCreate(BaseModel):
    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Expense title"
    )
    amount: float = Field(
        ...,
        gt=0,
        description="Expense amount"
    )
    category: Category
    date: date


class ExpenseResponse(BaseModel):
    id: int
    title: str
    amount: float
    category: Category
    date: date


class TotalResponse(BaseModel):
    total: float

class CategoryTotalResponse(BaseModel):
    category: Category
    total: float