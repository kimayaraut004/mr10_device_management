from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime


class CurrencyCreateSchema(BaseModel):
    name: str = Field(..., max_length=80)
    code: str = Field(..., min_length=3, max_length=3)
    countries: List[str] = Field(default_factory=list)
    is_enabled: bool = True


class CurrencyUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, max_length=80)
    countries: Optional[List[str]] = None
    is_enabled: Optional[bool] = None


class CurrencyResponseSchema(BaseModel):
    id: str
    name: str
    code: str
    countries: List[str]
    is_enabled: bool
    created_at: datetime
    updated_at: datetime
