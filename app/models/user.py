"""
app/models/user.py

SQLAlchemy ORM model for the users table.

This model defines the structure of every user account in AccessGuard AI.
Authentication, authorization, and access control decisions in future
phases will all reference this model.
"""

from datetime import datetime, timezone

from sqlalchemy import Boolean, DateTime, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class User(Base):
    """
    Represents a user account in the system.
    Maps to the 'users' table in PostgreSQL.
    """

    __tablename__ = "users"

    # Primary key — auto-incremented by PostgreSQL
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    # Login identity — both must be unique across all users
    username: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, index=True)
    email: Mapped[str] = mapped_column(
        String(255), unique=True, nullable=False, index=True)

    # Stores the bcrypt hash of the user's password, never the plaintext
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    # Controls whether the user can authenticate — defaults to active
    is_active: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=True)

    # Timezone-aware timestamps managed at the database level
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    )

    def __repr__(self) -> str:
        return f"<User id={self.id} username={self.username!r} active={self.is_active}>"
