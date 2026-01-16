from fastapi import (
    APIRouter,
    Request,
    Response,
    HTTPException,
    status,
    Depends,
    Query,
    Form,
    UploadFile,
    File,
)
import hashlib
import base64
from cryptography.fernet import Fernet
import json, secrets, string
from mongoengine.errors import NotUniqueError, DoesNotExist, ValidationError


from config import config
from core.currency_handler import currencyHandler
from core.token_handler import tokenHandler
from v1.serializers import *
from v1.response import *


router = APIRouter()


@router.post(
    "/currency",
    tags=["Currency"],
    status_code=status.HTTP_201_CREATED,
    # response_model=CurrencyResponseSchema,
)
def create_currency(
    data: CurrencyCreateSchema,
    # user_data: Dict = Depends(tokenHandler.authencticate_access_token),
):
    return {"detail": currencyHandler.create_currency(payload=data)}


@router.get(
    "/currency",
    tags=["Currency"],
)  # response_model=List[CurrencyResponseSchema]
def list_currencies(
    # user_data: Dict = Depends(tokenHandler.authencticate_access_token),
    limit: int = Query(50, le=200),
    skip: int = Query(0, ge=0),
):
    return {"detail": currencyHandler.fetch_currencies(limit=limit, skip=skip)}


@router.put(
    "/currency/{currency_id}",
    tags=["Currency"],
)  # response_model=CurrencyResponseSchema
def update_currency(
    currency_id: str,
    data: CurrencyUpdateSchema,
    # user_data: Dict = Depends(tokenHandler.authencticate_access_token),
):
    return {
        "detail": currencyHandler.update_currencies(
            currency_id=currency_id, payload=data
        )
    }


@router.delete(
    "/currency/{currency_id}", tags=["Currency"], status_code=status.HTTP_204_NO_CONTENT
)
def delete_currency(
    currency_id: str,
    # user_data: Dict = Depends(tokenHandler.authencticate_access_token),
):
    return {
        "detail": currencyHandler.delete_server_license_plan(currency_id=currency_id)
    }
