"""
app/models/permission.py

SQLAlchemy ORM model for the permissions table.

Permissions represent atomic business actions within AccessGuard AI.
Each permission follows the <action>_<resource> naming pattern:

    view_user, create_user, edit_user, delete_user
    assign_role, view_audit_log, export_audit_log

The RBAC system in future phases will link permissions to roles,
and roles to users, to make fine-grained access control decisions.

Important: permissions represent business actions, not implementation
details. For example, delete_user triggers a soft delete
(user.is_active = False), not a database row removal.
"""

from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class Permission(Base):
    """
    Represents a single, atomic business action in the system.
    Maps to the 'permissions' table in PostgreSQL.

    System permissions (is_system=True) are built-in and seeded at
    application startup. Their names are immutable once the application
    starts using them — changing a name would silently break every
    access control check that references it.
    """

    __tablename__ = "permissions"

    # Primary key — auto-incremented by PostgreSQL
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    # Internal permission identifier — unique, indexed, immutable after creation.
    # Must follow the <action>_<resource> pattern.
    # Examples: view_user, create_user, edit_user, delete_user,
    #           assign_role, view_audit_log, export_audit_log
    name: Mapped[str] = mapped_column(
        String(100), unique=True, nullable=False, index=True)

    # Human-readable explanation of what this permission allows — editable
    description: Mapped[str] = mapped_column(Text, nullable=False)

    # False by default at the database level — custom permissions created at
    # runtime are not system permissions.
    # Built-in permissions seeded at startup must explicitly set is_system=True.
    # The security layer will use this flag to block deletion or renaming.
    is_system: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default=func.false(),
    )

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
        return (
            f"<Permission id={self.id} name={self.name!r} system={self.is_system}>"
        )
