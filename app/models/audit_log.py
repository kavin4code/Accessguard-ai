"""
app/models/audit_log.py

SQLAlchemy ORM model for the audit_logs table.

AuditLog records immutable security events within AccessGuard AI.
Every significant action — logins, access denials, role changes,
permission modifications — produces one row in this table.

Architecture decisions:
- Rows are never updated or deleted after creation.
- Core event data belongs in dedicated typed columns.
- JSONB stores only optional, event-specific metadata.
- No ondelete — physical deletion is not valid in this system.
- No relationships — not implemented at this stage.

Example actions:
    LOGIN_SUCCESS, LOGIN_FAILED, CREATE_USER, UPDATE_USER,
    ASSIGN_ROLE, REMOVE_ROLE, ADD_PERMISSION, REMOVE_PERMISSION,
    ACCESS_DENIED, PASSWORD_CHANGED
"""

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class AuditLog(Base):
    """
    Records a single immutable security event.
    Maps to the 'audit_logs' table in PostgreSQL.

    Once written, a row is never modified. The application layer
    enforces immutability by only ever inserting into this table.
    """

    __tablename__ = "audit_logs"

    # Primary key — auto-incremented by PostgreSQL
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    # The authenticated user who triggered the event.
    # Non-null — every auditable event must be traceable to an actor.
    actor_user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    # Standardized event identifier.
    # Examples: LOGIN_SUCCESS, ACCESS_DENIED, ASSIGN_ROLE, PASSWORD_CHANGED
    action: Mapped[str] = mapped_column(
        String(100), nullable=False, index=True)

    # The type of entity affected by this event.
    # Examples: USER, ROLE, PERMISSION, ROLE_ASSIGNMENT
    resource_type: Mapped[str] = mapped_column(
        String(50), nullable=False, index=True)

    # The primary key of the affected entity.
    # Nullable — some events (e.g. LOGIN_FAILED before auth completes)
    # have no target resource to reference.
    resource_id: Mapped[int | None] = mapped_column(Integer, nullable=True)

    # Outcome of the event — SUCCESS or FAILED.
    status: Mapped[str] = mapped_column(String(20), nullable=False, index=True)

    # Optional event-specific metadata stored as JSONB.
    # Examples: {"ip_address": "192.168.1.1"} for LOGIN_FAILED,
    #           {"previous_role": "viewer"} for ASSIGN_ROLE.
    # Nullable — not all events carry additional metadata.
    details: Mapped[dict | None] = mapped_column(JSONB, nullable=True)

    # Set once by PostgreSQL at insert — never changes.
    # No updated_at — this table is immutable by design.
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    def __repr__(self) -> str:
        return (
            f"<AuditLog id={self.id} "
            f"actor={self.actor_user_id} "
            f"action={self.action!r} "
            f"status={self.status!r}>"
        )
