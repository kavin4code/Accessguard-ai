"""
app/database/session.py

Creates and exports the SessionLocal factory.

Each request gets its own Session instance created from this factory.
Sessions are opened at the start of a request and closed when it ends.
"""

from sqlalchemy.orm import sessionmaker, Session

from app.database.engine import engine

SessionLocal: sessionmaker[Session] = sessionmaker(
    bind=engine,
    # Do not commit automatically — commits must be explicit.
    # This keeps transactions predictable and prevents partial writes.
    autocommit=False,
    # Do not flush automatically before every query.
    # Gives explicit control over when changes are sent to the database.
    autoflush=False,
)
