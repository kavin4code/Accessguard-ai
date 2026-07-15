"""
app/database/base.py

Defines the declarative Base class for all SQLAlchemy models.

Every model in app/models/ inherits from Base:

    from app.database.base import Base

    class User(Base):
        __tablename__ = "users"
        ...

Base.metadata holds the table definitions and is used by Alembic
to generate and apply migrations.

All models must be imported below so SQLAlchemy registers them
in Base.metadata before any metadata operation is performed.
"""

from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Shared base class for all ORM models.
    Inheriting from DeclarativeBase is the SQLAlchemy 2.x recommended approach.
    """
    pass


# Model imports — required so SQLAlchemy registers each table in Base.metadata.
# Add every new model here as it is created in future phases.
from app.models.user import User              # noqa: E402, F401
from app.models.role import Role              # noqa: E402, F401
from app.models.permission import Permission  # noqa: E402, F401
