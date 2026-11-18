from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    SECRET_KEY: SecretStr # Secret key used for JWT token encoding and decoding
    ALGORITHM: str = "HS256" # Algorithm used for JWT token encoding and decoding
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30 # Minutes

    max_upload_size_bytes: int = 5 * 1024 * 1024 # 5 MB

settings = Settings() # Loaded from .env file