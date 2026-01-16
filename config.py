import os
import socket


class Config:
    def __init__(self, **kwargs) -> None:
        self.ENVIRONMENT = kwargs["ENVIRONMENT"]
        self.SERVICE_NAME = kwargs["SERVICE_NAME"]
        self.SERVICE_DESCRIPTION = kwargs["SERVICE_DESCRIPTION"]
        self.VERSION = kwargs["VERSION"]
        self.SUBROUTE = kwargs["SUBROUTE"]
        self.MY_IP = kwargs["MY_IP"]

        self.DATABASE_NAME = kwargs["DATABASE_NAME"]
        self.DATABASE_USERNAME = kwargs["DATABASE_USERNAME"]
        self.DATABASE_PASSWORD = kwargs["DATABASE_PASSWORD"]
        self.DATABASE_HOST = kwargs["DATABASE_HOST"]
        self.DATABASE_AUTHENTICATION_SOURCE = kwargs["DATABASE_AUTHENTICATION_SOURCE"]

        self.SECRET_KEY = kwargs["SECRET_KEY"]
        self.ALGORITHM = kwargs["ALGORITHM"]

        self.KAFKA_SERVERS = kwargs["KAFKA_SERVERS"]
        self.KAFKA_SECURITY_PROTOCOL = kwargs["KAFKA_SECURITY_PROTOCOL"]
        self.KAFKA_SASL_USERNAME = kwargs["KAFKA_SASL_USERNAME"]
        self.KAFKA_SASL_PASSWORD = kwargs["KAFKA_SASL_PASSWORD"]
        self.KAFKA_SASL_MECHANISM = kwargs["KAFKA_SASL_MECHANISM"]
        self.KAFKA_AUTO_OFFSET_RESET = kwargs["KAFKA_AUTO_OFFSET_RESET"]
        self.KAFKA_CONSUMER_GROUP = kwargs["KAFKA_CONSUMER_GROUP"]

        self.KEY_SIZE = kwargs["KEY_SIZE"]
        self.BLOCK_SIZE = kwargs["BLOCK_SIZE"]
        self.ITERATIONS = kwargs["ITERATIONS"]
        self.SALT_SIZE = kwargs["SALT_SIZE"]
        self.LICENSE_KEY_LENGTH = kwargs["LICENSE_KEY_LENGTH"]


config = Config(
    ENVIRONMENT=os.getenv("ENVIRONMENT", "dev"),
    SERVICE_NAME="device_management",
    SERVICE_DESCRIPTION="service to manage device licensing and authentication in marketplace",
    VERSION="0.0.1",
    SUBROUTE="device",
    DATABASE_NAME="device_management_db",
    DATABASE_USERNAME=os.getenv("DATABASE_USERNAME", "redx"),
    DATABASE_PASSWORD=os.getenv("DATABASE_PASSWORD", "XPp187QYjEjP5KP"),
    DATABASE_HOST=os.getenv("DATABASE_HOST", "mongo"),
    DATABASE_AUTHENTICATION_SOURCE=os.getenv("DATABASE_AUTHENTICATION_SOURCE", "admin"),
    MY_IP=os.getenv("ip", "192.168.1.16"),
    SECRET_KEY="gRTIYbKM5TTmVNGCMTCwQKtZbc8b9xQ9",
    ALGORITHM="HS256",
    KAFKA_SERVERS=os.getenv("KAFKA_HOST", "kafka"),
    KAFKA_SECURITY_PROTOCOL="SASL_PLAINTEXT",
    KAFKA_SASL_USERNAME="admin",
    KAFKA_SASL_PASSWORD="admin-secret",
    KAFKA_SASL_MECHANISM="PLAIN",
    KAFKA_AUTO_OFFSET_RESET="latest",
    KAFKA_CONSUMER_GROUP="device_management",
    KEY_SIZE=32,
    BLOCK_SIZE=16,
    ITERATIONS=100000,
    SALT_SIZE=16,
    LICENSE_KEY_LENGTH=16,
)
