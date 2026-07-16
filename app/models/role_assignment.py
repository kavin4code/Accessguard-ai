"""
app/models/role_assignment.py

SQLAlchemy ORM model for the role_assignments table.

A RoleAssignment records the business event of granting a role to a user.
It is not a plain junction table — every assignment captures who performed
the grant and when, providing a full audit trail for all role changes.

Architecture decisions:
- Users are never physically deleted (soft delete via is_active).
- Therefore no ondelete behavior is specified on any foreign key.
- Relationships are not implemented at this stage.
"""

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class RoleAssignment(Base):
    """
    Records the assignment of a role to a user.
    Maps to the 'role_assignments' table in PostgreSQL.

    The UNIQUE constraint on (user_id, role_id) ensures the same role
    cannot be assigned to the same user more than once.
    """

    __tablename__ = "role_assignments"

    __table_args__ = (
        # Prevents duplicate assignments of the same role to the same user.
        # Enforced at the database level — cannot be bypassed by application logic.
        UniqueConstraint("user_id", "role_id",
                         name="uq_role_assignments_user_role"),
    )

    # Primary key — auto-incremented by PostgreSQL
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    # The user receiving the role
    user_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    # The role being granted
    role_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("roles.id"),
        nullable=False,
        index=True,
    )

    # The user who performed the assignment — required for audit trail
    assigned_by: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("users.id"),
        nullable=False,
        index=True,
    )

    # Set once by PostgreSQL at insert — permanent record of when the assignment occurred
    assigned_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    def __repr__(self) -> str:
        return (
            f"<RoleAssignment id={self.id} "
            f"user_id={self.user_id} "
            f"role_id={self.role_id} "
            f"assigned_by={self.assigned_by}>"
        )
