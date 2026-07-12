"""
app/database/engine.py

Creates and exports the SQLAlchemy Engine.

The engine manages the connection pool to PostgreSQL.
It is created once at startup and shared across the entire application.
"""

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from app.core.config import settings

engine: Engine = create_engine(
    settings.DATABASE_URL,
    # Return connections to the pool after 30 minutes of inactivity.
    # Prevents stale connections when PostgreSQL closes idle sessions.
    pool_recycle=1800,
    # Verify the connection is still alive before using it from the pool.
    pool_pre_ping=True,
    # Log all SQL statements when DEBUG is enabled.
    echo=settings.DEBUG,
)
