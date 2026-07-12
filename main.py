"""
main.py

Entry point for AccessGuard AI.
Creates the FastAPI application and registers the root and health endpoints.

Phase 0: skeleton only.
No database, no authentication, no middleware.
"""

from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=(
        "A cybersecurity platform for demonstrating and preventing "
        "OWASP A01:2025 Broken Access Control vulnerabilities."
    ),
    debug=settings.DEBUG,
)


@app.get("/", tags=["Health"])
def root() -> dict:
    """
    Root endpoint.
    Confirms the application is running and returns its name and version.
    """
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


@app.get("/health", tags=["Health"])
def health_check() -> dict:
    """
    Health-check endpoint.
    Used to verify the server is reachable and responsive.
    """
    return {"status": "ok"}
