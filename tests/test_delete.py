from conftest import client


def test_delete_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 350,
            "category": "Food",
            "date": "2026-08-03"
        }
    )

    expense_id = response.json()["id"]

    delete_response = client.delete(f"/expenses/{expense_id}")

    assert delete_response.status_code == 200
    assert delete_response.json()["message"] == "Expense deleted successfully"

    get_response = client.get("/expenses")

    assert len(get_response.json()) == 0


def test_delete_non_existing_expense():
    response = client.delete("/expenses/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Expense not found"