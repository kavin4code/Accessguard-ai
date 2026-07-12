"""
app/database/dependencies.py

Provides the get_db() dependency for FastAPI route handlers.

Usage in any route:

    from sqlalchemy.orm import Session
    from fastapi import Depends
    from app.database.dependencies import get_db

    @router.get("/example")
    def example_route(db: Session = Depends(get_db)):
        ...

get_db() opens a session at the start of each request and guarantees
it is closed when the request ends, whether it succeeds or raises an exception.
"""

from collections.abc import Generator

from sqlalchemy.orm import Session

from app.database.session import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """
    Yield a database session for the duration of a single request.

    The finally block ensures the session is always closed,
    preventing connection leaks regardless of whether the request
    succeeds or raises an exception.
    """
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
