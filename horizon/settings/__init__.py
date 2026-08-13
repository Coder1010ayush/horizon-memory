"""Settings management — env vars, config defaults, validation."""

from __future__ import annotations

from pathlib import Path

# Base directories
PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent
HORIZON_DATA_DIR: Path = Path(".horizon/data")

# API defaults
API_HOST: str = "127.0.0.1"
API_PORT: int = 8765

# Logging
LOG_LEVEL: str = "INFO"

# DB defaults
DEFAULT_VECTOR_BACKEND: str = "lancedb"
DEFAULT_GRAPH_BACKEND: str = "kuzu"
DEFAULT_RELATIONAL_BACKEND: str = "sqlite"

__all__ = [
    "PROJECT_ROOT",
    "HORIZON_DATA_DIR",
    "API_HOST",
    "API_PORT",
    "LOG_LEVEL",
    "DEFAULT_VECTOR_BACKEND",
    "DEFAULT_GRAPH_BACKEND",
    "DEFAULT_RELATIONAL_BACKEND",
]
