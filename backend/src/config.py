from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import ConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
    # Database
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    
    # API
    API_HOST: str
    API_PORT: int
    API_RELOAD: bool
    API_TITLE: str
    API_DESCRIPTION: str
    API_VERSION: str
    CORS_ORIGINS: list

    # JWT Settings
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int
settings = Settings()
