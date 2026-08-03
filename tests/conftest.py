import json
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# Add the src directory to Python's module search path
SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from main import app

client = TestClient(app)

DATA_FILE = Path(__file__).resolve().parent.parent / "expenses.json"


@pytest.fixture(autouse=True)
def reset_expenses():
    """
    Reset expenses.json before each test.
    """
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump([], file)

    yield

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump([], file)