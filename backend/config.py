from pydantic_settings import BaseSettings
from typing import List
import os


class Settings(BaseSettings):
    """Application configuration"""
    
    # API
    API_TITLE: str = "ET GenAI Backend"
    API_VERSION: str = "1.0.0"
    
    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    
    # Database
    MONGO_URI: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "et_genai_db"
    
    # Collections
    TASKS_COLLECTION: str = "tasks"
    LOGS_COLLECTION: str = "logs"
    
    class Config:
        env_file = ".env"
        extra = "ignore"  # Ignore extra fields from .env
    
    @property
    def CORS_ORIGINS(self) -> List[str]:
        """CORS origins for frontend"""
        return [
            "http://localhost:3000",
            "http://localhost:8000",
            "http://127.0.0.1:3000",
            "http://127.0.0.1:8000"
        ]


settings = Settings()
