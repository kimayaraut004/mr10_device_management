from fastapi import Depends, HTTPException, status, Request, Response, UploadFile
from fastapi.responses import StreamingResponse
from bson import ObjectId
from mongoengine.errors import ValidationError as MongoValidationError
import base64, hashlib, json
from cryptography.fernet import Fernet
from io import BytesIO

from v1.serializers import *
from v1.models import *
from core.logger import console_logger


class CurrencyHandler:
    def __init__(self) -> None:
        pass

    def create_currency(self, payload) -> dict:
        """
        Creates a new currency entry.

        - Normalizes currency code and countries
        - Saves to MongoDB
        - Returns API payload

        Args:
            payload (CurrencyCreateSchema)

        Returns:
            dict: Currency payload
        """
        try:
            doc = CurrencySetting(**payload.dict())

            # Normalize
            doc.code = doc.code.upper().strip()
            doc.countries = [c.upper().strip() for c in (doc.countries or [])]

            doc.save()
            return doc.payload()

        except NotUniqueError:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Currency code already exists",
            )

        except ValidationError as e:
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
                detail=str(e),
            )

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unable to create currency {e}",
            )

    def fetch_currencies(self, limit: int, skip: int) -> List[dict]:
        """
        Fetch paginated list of currencies sorted by currency code.

        Args:
            limit (int): Max records to return
            skip (int): Records to skip

        Returns:
            List[dict]: List of currency payloads
        """
        try:
            currencies = (
                CurrencySetting.objects().order_by("code").skip(skip).limit(limit)
            )

            return [c.payload() for c in currencies]

        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Unable to fetch currencies",
            )

    def update_currencies(self, currency_id: str, payload) -> dict:
        try:
            doc = CurrencySetting.objects.get(id=currency_id)
            updates = {k: v for k, v in payload.dict().items() if v is not None}
            for k, v in updates.items():
                setattr(doc, k, v)
            doc.save()
            return doc.payload()
        except DoesNotExist:
            raise HTTPException(status_code=404, detail="Currency not found")
        except ValidationError as e:
            raise HTTPException(status_code=400, detail=str(e))

    def delete_server_license_plan(self, currency_id: str) -> None:
        deleted = CurrencySetting.objects(id=currency_id).delete()

        if not deleted:
            raise HTTPException(status_code=404, detail="Currency not found")


currencyHandler = CurrencyHandler()
