"""
app/core/config.py

Central configuration for AccessGuard AI.
Reads environment variables from .env using python-dotenv.

Usage anywhere in the project:
    from app.core.config import settings
"""

import os

from dotenv import load_dotenv

# Load .env into os.environ before anything reads from it
load_dotenv()


class Settings:
    """Application settings loaded from environment variables."""

    # Application
    APP_NAME: str = os.getenv("APP_NAME", "AccessGuard AI")
    APP_VERSION: str = os.getenv("APP_VERSION", "0.1.0")
    DEBUG: bool = os.getenv("DEBUG", "true").lower() == "true"

    # Server
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", "8000"))

    # Database
    DATABASE_URL: str = os.environ["DATABASE_URL"]


# Shared instance — import this everywhere, never instantiate Settings directly
settings = Settings()
