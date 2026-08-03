from conftest import client


def test_get_all_expenses():
    # Add first expense
    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 350,
            "category": "Food",
            "date": "2026-08-03"
        }
    )

    # Add second expense
    client.post(
        "/expenses",
        json={
            "title": "Bus Ticket",
            "amount": 100,
            "category": "Travel",
            "date": "2026-08-04"
        }
    )

    response = client.get("/expenses")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2

    assert data[0]["title"] == "Pizza"
    assert data[1]["title"] == "Bus Ticket"


def test_filter_expenses_by_category():
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
            "title": "Movie",
            "amount": 500,
            "category": "Entertainment",
            "date": "2026-08-04"
        }
    )

    response = client.get("/expenses/category/Food")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 1
    assert data[0]["category"] == "Food"