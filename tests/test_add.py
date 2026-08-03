from conftest import client


def test_add_expense():
    response = client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 350,
            "category": "Food",
            "date": "2026-08-03"
        }
    )

    assert response.status_code == 201

    data = response.json()

    assert data["id"] == 1
    assert data["title"] == "Pizza"
    assert data["amount"] == 350
    assert data["category"] == "Food"
    assert data["date"] == "2026-08-03"