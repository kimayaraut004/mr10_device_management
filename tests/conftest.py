import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from v1 import app


@pytest.fixture(scope="function")
def test_client():
    with patch(
        "core.currency_handler.currencyHandler.create_currency"
    ) as m_create, patch(
        "core.currency_handler.currencyHandler.fetch_currencies"
    ) as m_list, patch(
        "core.currency_handler.currencyHandler.update_currencies"
    ) as m_update, patch(
        "core.currency_handler.currencyHandler.delete_server_license_plan"
    ) as m_delete:

        # SUCCESS responses
        m_create.return_value = {
            "id": "507f1f77bcf86cd799439011",
            "name": "US Dollar",
            "code": "USD",
            "countries": ["USA", "ECUADOR"],
            "is_enabled": True,
            "created_at": "2026-01-14T10:00:00Z",
            "updated_at": "2026-01-14T10:00:00Z",
        }
        m_list.return_value = [
            {"id": "507f1f77bcf86cd799439011", "name": "US Dollar", "code": "USD"}
        ]
        m_update.return_value = {
            "id": "507f1f77bcf86cd799439011",
            "name": "United States Dollar",
            "code": "USD",
        }
        m_delete.return_value = None

        with TestClient(app, raise_server_exceptions=False) as client:
            yield client


@pytest.fixture()
def currency_payload():
    return {"name": "US Dollar", "code": "USD", "countries": ["USA", "ECUADOR"]}


@pytest.fixture()
def currency_payload_updated():
    return {
        "name": "United States Dollar",
        "countries": ["USA", "PANAMA"],
        "is_enabled": False,
    }
