"""
app/models/role_permission.py

SQLAlchemy ORM model for the role_permissions table.

RolePermission defines the current RBAC policy by linking roles to
permissions. It answers one question only:

    "Which permissions belong to which roles?"

This is a policy table, not an audit table. It reflects the current
state of the RBAC configuration. Audit history for policy changes
will be handled by the AuditLog model in a future phase.

Architecture decisions:
- No timestamps — this table records policy state, not events.
- No audit fields — audit history belongs in AuditLog.
- No relationships — not implemented at this stage.
- No ondelete — physical deletion is not a valid operation in this system.
"""

from sqlalchemy import ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


class RolePermission(Base):
    """
    Links a role to a permission, defining the current RBAC policy.
    Maps to the 'role_permissions' table in PostgreSQL.

    The UNIQUE constraint on (role_id, permission_id) ensures the same
    permission cannot be assigned to the same role more than once.
    """

    __tablename__ = "role_permissions"

    __table_args__ = (
        # Prevents duplicate permission entries for the same role.
        # Enforced at the database level — cannot be bypassed by application logic.
        UniqueConstraint(
            "role_id",
            "permission_id",
            name="uq_role_permissions_role_permission",
        ),
    )

    # Primary key — auto-incremented by PostgreSQL
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True)

    # The role receiving the permission
    role_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("roles.id"),
        nullable=False,
        index=True,
    )

    # The permission being granted to the role
    permission_id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("permissions.id"),
        nullable=False,
        index=True,
    )

    def __repr__(self) -> str:
        return (
            f"<RolePermission id={self.id} "
            f"role_id={self.role_id} "
            f"permission_id={self.permission_id}>"
        )
