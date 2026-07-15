"""
app/models/role.py

SQLAlchemy ORM model for the roles table.

Roles represent named permission levels within AccessGuard AI.
Future phases will assign roles to users and use them to enforce
access control decisions across the application.
"""

from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Role(Base):
    """
    Represents a permission level that can be assigned to users.
    Maps to the 'roles' table in PostgreSQL.

    System roles (is_system=True) are built-in and must not be
    renamed or deleted by the application.
    """

    __tablename__ = "roles"

    # Primary key — auto-incremented by PostgreSQL
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    # Internal role identifier — unique, indexed, treated as immutable after creation
    # Examples: "administrator", "analyst", "viewer"
    name: Mapped[str] = mapped_column(
        String(50), unique=True, nullable=False, index=True)

    # Human-readable explanation of what this role permits — editable
    description: Mapped[str] = mapped_column(Text, nullable=False)

    # False by default — custom roles created at runtime are not system roles.
    # Built-in roles seeded at startup must explicitly set this to True.
    # The security layer will use this flag to block deletion or renaming of system roles.
    # Treated as immutable after the row is created.
    is_system: Mapped[bool] = mapped_column(
        Boolean, nullable=False, default=False)

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
        return f"<Role id={self.id} name={self.name!r} system={self.is_system}>"
