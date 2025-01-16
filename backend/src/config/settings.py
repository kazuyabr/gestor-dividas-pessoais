from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from dotenv import load_dotenv

# Garante que as variáveis de ambiente sejam carregadas
load_dotenv()

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    
    # Database
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")
    
    # API
    API_HOST: str = os.getenv("API_HOST")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    API_RELOAD: bool = os.getenv("API_RELOAD", "True").lower() == "true"
    API_TITLE: str = os.getenv("API_TITLE")
    API_DESCRIPTION: str = os.getenv("API_DESCRIPTION")
    API_VERSION: str = os.getenv("API_VERSION")
    CORS_ORIGINS: list = os.getenv("CORS_ORIGINS", "[]")

    # JWT Settings
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    # Logging
    log_level: str = os.getenv("LOG_LEVEL")
    log_format: str = os.getenv("LOG_FORMAT")
    log_dir: str = os.getenv("LOG_DIR")
    enable_access_logs: bool = os.getenv("ENABLE_ACCESS_LOGS", "True").lower() == "true"
    enable_error_logs: bool = os.getenv("ENABLE_ERROR_LOGS", "True").lower() == "true"

settings = Settings()
