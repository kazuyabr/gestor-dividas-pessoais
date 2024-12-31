from pydantic_settings import BaseSettings

class Settings(BaseSettings):
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

    class Config:
        env_file = ".env"

settings = Settings()
