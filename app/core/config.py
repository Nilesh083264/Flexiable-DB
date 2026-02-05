"""
File: app/core/config.py
Responsibility: Centralized application configuration management
"""

import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # Application
    APP_NAME: str = os.getenv("APP_NAME", "Flexible Database")
    ENV: str = os.getenv("ENV", "dev")

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    LOG_DIR: str = os.getenv("LOG_DIR", "logs")

    # Database engine
    DB_TYPE: str = os.getenv("DB_TYPE", "mongo")

    # MongoDB
    MONGO_URI: str = os.getenv(
        "MONGO_URI", "mongodb://localhost:27017"
    )

    # PostgreSQL
    POSTGRES_HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: int = int(os.getenv("POSTGRES_PORT", 5432))
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "flexdb")
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")


settings = Settings()
