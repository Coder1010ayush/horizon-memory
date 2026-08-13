"""FastAPI application factory for Horizon Memory."""

from fastapi import FastAPI

__all__ = ["create_app"]


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(
        title="Horizon Memory API",
        description="The memory layer that understands your data",
        version="0.1.0",
    )

    @app.get("/health")
    async def health():
        return {"status": "ok", "version": "0.1.0"}

    return app
