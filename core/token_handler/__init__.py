from fastapi import Depends, HTTPException
from fastapi.security.http import HTTPBase
from jose import jwt

from config import config
from core.logger import console_logger


class TokenHandler:
    def __init__(self) -> None:
        pass

    def decode_token(self, token):
        try:
            return jwt.decode(token, config.SECRET_KEY, algorithms=config.ALGORITHM)
        except Exception as e:
            console_logger.debug(e)
            raise HTTPException(status_code=401)

    def authencticate_access_token(
        self, token: str = Depends(HTTPBase(scheme="Bearer"))
    ):
        token_data = self.decode_token(token.credentials)
        return token_data



tokenHandler = TokenHandler()
