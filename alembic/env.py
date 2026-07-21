"""
alembic/env.py

Alembic migration environment for AccessGuard AI.

Architecture Decision #14:
    The database URL is obtained from app/core/config.py (which reads
    from .env) — never from alembic.ini. There is one source of truth
    for the database connection string.

How autogeneration works:
    Alembic compares Base.metadata (the Python model definitions)
    against the live database schema and generates the SQL needed
    to bring them in sync.
"""

from app.database.base import Base
from app.core.config import settings
from sqlalchemy import engine_from_config, pool
from alembic import context
from pathlib import Path
import sys
from logging.config import fileConfig

# ---------------------------------------------------------------------------
# Make the project root importable BEFORE importing application modules
# ---------------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


# ---------------------------------------------------------------------------
# Application imports
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# Alembic configuration
# ---------------------------------------------------------------------------

config = context.config

# Use the application's database URL instead of alembic.ini
config.set_main_option(
    "sqlalchemy.url",
    str(settings.DATABASE_URL),
)

# Configure logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata used for autogeneration
target_metadata = Base.metadata


# ---------------------------------------------------------------------------
# Offline migrations
# ---------------------------------------------------------------------------

def run_migrations_offline() -> None:
    """
    Run migrations without connecting to the database.
    Generates SQL scripts only.
    """

    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
    )

    with context.begin_transaction():
        context.run_migrations()


# ---------------------------------------------------------------------------
# Online migrations
# ---------------------------------------------------------------------------

def run_migrations_online() -> None:
    """
    Run migrations while connected to the database.
    """

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
