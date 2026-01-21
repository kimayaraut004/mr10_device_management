import os
from dotenv import load_dotenv

# Load .env file (local dev) or use GitHub Actions env vars (CI/CD)
load_dotenv()

class Config:
    def __init__(self, **kwargs) -> None:
        self.ENVIRONMENT = kwargs.get("ENVIRONMENT", os.getenv("ENVIRONMENT", "dev"))
        self.SERVICE_NAME = kwargs.get("SERVICE_NAME", os.getenv("SERVICE_NAME", "device_management"))
        self.SERVICE_DESCRIPTION = kwargs.get("SERVICE_DESCRIPTION", os.getenv("SERVICE_DESCRIPTION", "device service"))
        self.VERSION = kwargs.get("VERSION", os.getenv("VERSION", "0.0.1"))
        self.SUBROUTE = kwargs.get("SUBROUTE", os.getenv("SUBROUTE", "device"))
        self.MY_IP = kwargs.get("MY_IP", os.getenv("MY_IP", "192.168.1.16"))

        # Database (SENSITIVE - GitHub Secrets)
        self.DATABASE_NAME = kwargs.get("DATABASE_NAME", os.getenv("DATABASE_NAME", "device_management_db"))
        self.DATABASE_USERNAME = kwargs.get("DATABASE_USERNAME") or os.getenv("DATABASE_USERNAME")
        self.DATABASE_PASSWORD = kwargs.get("DATABASE_PASSWORD") or os.getenv("DATABASE_PASSWORD")
        self.DATABASE_HOST = kwargs.get("DATABASE_HOST", os.getenv("DATABASE_HOST", "mongo"))
        self.DATABASE_AUTHENTICATION_SOURCE = kwargs.get("DATABASE_AUTHENTICATION_SOURCE", os.getenv("DATABASE_AUTHENTICATION_SOURCE", "admin"))

        # JWT (SENSITIVE)
        self.SECRET_KEY = kwargs.get("SECRET_KEY") or os.getenv("SECRET_KEY")
        self.ALGORITHM = kwargs.get("ALGORITHM", os.getenv("ALGORITHM", "HS256"))

        # Kafka (SENSITIVE)
        self.KAFKA_SERVERS = kwargs.get("KAFKA_SERVERS", os.getenv("KAFKA_SERVERS", "kafka"))
        self.KAFKA_SECURITY_PROTOCOL = kwargs.get("KAFKA_SECURITY_PROTOCOL", os.getenv("KAFKA_SECURITY_PROTOCOL", "SASL_PLAINTEXT"))
        self.KAFKA_SASL_USERNAME = kwargs.get("KAFKA_SASL_USERNAME") or os.getenv("KAFKA_SASL_USERNAME")
        self.KAFKA_SASL_PASSWORD = kwargs.get("KAFKA_SASL_PASSWORD") or os.getenv("KAFKA_SASL_PASSWORD")
        self.KAFKA_SASL_MECHANISM = kwargs.get("KAFKA_SASL_MECHANISM", os.getenv("KAFKA_SASL_MECHANISM", "PLAIN"))
        self.KAFKA_AUTO_OFFSET_RESET = kwargs.get("KAFKA_AUTO_OFFSET_RESET", os.getenv("KAFKA_AUTO_OFFSET_RESET", "latest"))
        self.KAFKA_CONSUMER_GROUP = kwargs.get("KAFKA_CONSUMER_GROUP", os.getenv("KAFKA_CONSUMER_GROUP", "device_management"))

        # Crypto
        self.KEY_SIZE = kwargs.get("KEY_SIZE", os.getenv("KEY_SIZE", 32))
        self.BLOCK_SIZE = kwargs.get("BLOCK_SIZE", os.getenv("BLOCK_SIZE", 16))
        self.ITERATIONS = kwargs.get("ITERATIONS", os.getenv("ITERATIONS", 100000))
        self.SALT_SIZE = kwargs.get("SALT_SIZE", os.getenv("SALT_SIZE", 16))
        self.LICENSE_KEY_LENGTH = kwargs.get("LICENSE_KEY_LENGTH", os.getenv("LICENSE_KEY_LENGTH", 16))

# Global config instance
config = Config()
