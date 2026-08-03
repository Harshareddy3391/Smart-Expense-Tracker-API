from conftest import client


def test_total_expenses():
    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 350,
            "category": "Food",
            "date": "2026-08-03"
        }
    )

    client.post(
        "/expenses",
        json={
            "title": "Bus Ticket",
            "amount": 100,
            "category": "Travel",
            "date": "2026-08-04"
        }
    )

    response = client.get("/expenses/total")

    assert response.status_code == 200

    data = response.json()

    assert data["total"] == 450


def test_total_by_category():
    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 350,
            "category": "Food",
            "date": "2026-08-03"
        }
    )

    client.post(
        "/expenses",
        json={
            "title": "Burger",
            "amount": 150,
            "category": "Food",
            "date": "2026-08-04"
        }
    )

    client.post(
        "/expenses",
        json={
            "title": "Movie",
            "amount": 500,
            "category": "Entertainment",
            "date": "2026-08-05"
        }
    )

    response = client.get("/expenses/total/Food")

    assert response.status_code == 200

    data = response.json()

    assert data["category"] == "Food"
    assert data["total"] == 500