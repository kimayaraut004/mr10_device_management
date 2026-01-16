from mongoengine import *
from datetime import datetime
from config import config


class CurrencySetting(Document):
    name = StringField(required=True, max_length=80)
    code = StringField(required=True, min_length=3, max_length=3, unique=True)
    is_enabled = BooleanField(default=True)

    countries = ListField(StringField(min_length=0, max_length=50), default=list)

    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    _version = StringField(default=config.VERSION)
    meta = {
        "collection": "currency_settings",
        "indexes": ["code"],  # unique index also created by unique=True
    }

    def payload(self):
        return {
            "id": str(self.id) if self.id else None,
            "name": self.name,
            "code": self.code,
            "countries": self.countries or [],
            "is_enabled": self.is_enabled,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }
