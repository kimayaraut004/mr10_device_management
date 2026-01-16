import pytest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from unittest.mock import patch, MagicMock
from fastapi import HTTPException, status
from core.currency_handler import CurrencyHandler
from v1.serializers import CurrencyCreateSchema, CurrencyUpdateSchema
from v1.models import CurrencySetting
from mongoengine.errors import NotUniqueError, DoesNotExist


@pytest.fixture
def currency_handler():
    return CurrencyHandler()


@pytest.fixture
def valid_create_payload():
    return CurrencyCreateSchema(
        name="US Dollar", code="USD", countries=["USA", "ECUADOR"]
    )


@pytest.fixture
def valid_update_payload():
    return CurrencyUpdateSchema(
        name="United States Dollar", countries=["USA", "PANAMA"]
    )


@pytest.fixture
def mock_currency_doc():
    """Mock CurrencySetting document with proper attributes."""
    mock_doc = MagicMock()
    mock_doc.id = "507f1f77bcf86cd799439011"

    # Set initial values BEFORE mocking methods
    mock_doc.code = "usd"  # Will be set to "USD" by normalization
    mock_doc.countries = ["usa", "ecuador"]  # Will be normalized

    # Mock methods
    mock_doc.payload.return_value = {
        "id": "507f1f77bcf86cd799439011",
        "name": "US Dollar",
        "code": "USD",
        "countries": ["USA", "ECUADOR"],
        "is_enabled": True,
    }
    mock_doc.save.return_value = None

    return mock_doc


class TestCurrencyHandler:

    def test_create_currency_success(
        self, currency_handler, valid_create_payload, mock_currency_doc
    ):
        with patch("core.currency_handler.CurrencySetting") as MockCurrencySetting:
            MockCurrencySetting.return_value = mock_currency_doc

            result = currency_handler.create_currency(valid_create_payload)

            # Verify save was called (no real DB)
            mock_currency_doc.save.assert_called_once()

            # Verify payload returned correctly
            assert result["name"] == "US Dollar"
            assert result["code"] == "USD"
            mock_currency_doc.payload.assert_called_once()

    def test_create_currency_duplicate(self, currency_handler, valid_create_payload):
        with patch("core.currency_handler.CurrencySetting") as MockCurrencySetting:
            mock_doc = MagicMock()
            mock_doc.save.side_effect = NotUniqueError("Duplicate USD")
            MockCurrencySetting.return_value = mock_doc

            with pytest.raises(HTTPException) as exc_info:
                currency_handler.create_currency(valid_create_payload)

            assert exc_info.value.status_code == 409

    def test_fetch_currencies_success(self, currency_handler):
        mock_doc1 = MagicMock()
        mock_doc1.payload.return_value = {"id": "1", "name": "USD", "code": "USD"}
        mock_doc2 = MagicMock()
        mock_doc2.payload.return_value = {"id": "2", "name": "EUR", "code": "EUR"}

        with patch("core.currency_handler.CurrencySetting.objects") as mock_objects:
            mock_objects.return_value.order_by.return_value.skip.return_value.limit.return_value = [
                mock_doc1,
                mock_doc2,
            ]

            result = currency_handler.fetch_currencies(limit=10, skip=0)

            assert len(result) == 2
            mock_doc1.payload.assert_called_once()
            mock_doc2.payload.assert_called_once()

    def test_update_currency_success(self, currency_handler, valid_update_payload):
        test_id = "507f1f77bcf86cd799439011"

        # Mock the entire objects chain
        mock_doc = MagicMock()
        mock_doc.payload.return_value = {
            "id": test_id,
            "name": "United States Dollar",
            "code": "USD",
        }
        mock_doc.save.return_value = None

        with patch("core.currency_handler.CurrencySetting.objects") as mock_objects:
            # Mock the entire chain: objects → get → return mock_doc
            mock_objects.get.return_value = mock_doc

            result = currency_handler.update_currencies(test_id, valid_update_payload)

            mock_doc.save.assert_called_once()
            assert result["name"] == "United States Dollar"

    def test_update_currency_not_found(self, currency_handler):
        test_id = "507f1f77bcf86cd799439011"

        with patch("core.currency_handler.CurrencySetting.objects") as mock_objects:
            mock_objects.get.side_effect = DoesNotExist("Not found")

            with pytest.raises(HTTPException) as exc_info:
                currency_handler.update_currencies(
                    test_id, CurrencyUpdateSchema(name="Test")
                )
            assert exc_info.value.status_code == 404

    def test_delete_currency_success(self, currency_handler):
        test_id = "507f1f77bcf86cd799439011"

        with patch("core.currency_handler.CurrencySetting.objects") as mock_objects:
            mock_objects.return_value.delete.return_value = 1

            result = currency_handler.delete_server_license_plan(test_id)

            assert result is None

    def test_delete_currency_not_found(self, currency_handler):
        test_id = "507f1f77bcf86cd799439011"

        with patch("core.currency_handler.CurrencySetting.objects") as mock_objects:
            mock_objects.return_value.delete.return_value = 0

            with pytest.raises(HTTPException) as exc_info:
                currency_handler.delete_server_license_plan(test_id)
            assert exc_info.value.status_code == 404
