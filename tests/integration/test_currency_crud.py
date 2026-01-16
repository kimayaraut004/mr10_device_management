import pytest
import time


def test_create_currency(test_client, currency_payload):
    response = test_client.post("/api/v1/device/currency", json=currency_payload)
    assert response.status_code == 201
    data = response.json()["detail"]
    assert data["name"] == "US Dollar"
    assert data["code"] == "USD"


def test_list_currencies(test_client):
    response = test_client.get("/api/v1/device/currency")
    assert response.status_code == 200
    data = response.json()["detail"]
    assert isinstance(data, list)


def test_create_update_currency(
    test_client, currency_payload, currency_payload_updated
):
    response = test_client.post("/api/v1/device/currency", json=currency_payload)
    assert response.status_code == 201
    created_id = response.json()["detail"]["id"]

    time.sleep(0.1)
    response = test_client.put(
        f"/api/v1/device/currency/{created_id}", json=currency_payload_updated
    )
    assert response.status_code == 200


def test_create_delete_currency(test_client, currency_payload):
    response = test_client.post("/api/v1/device/currency", json=currency_payload)
    assert response.status_code == 201
    created_id = response.json()["detail"]["id"]

    response = test_client.delete(f"/api/v1/device/currency/{created_id}")
    assert response.status_code == 204


def test_update_currency(test_client, currency_payload_updated):
    response = test_client.put(
        "/api/v1/device/currency/507f1f77bcf86cd799439011",
        json=currency_payload_updated,
    )
    assert response.status_code == 200


def test_delete_currency(test_client):
    response = test_client.delete("/api/v1/device/currency/507f1f77bcf86cd799439011")
    assert response.status_code == 204
