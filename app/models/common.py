"""Modelos comunes: paginación y respuestas de error."""

from pydantic import BaseModel
from typing import Any


class PaginatedResponse(BaseModel):
    """Respuesta paginada genérica."""
    data: list[Any]
    page: int
    limit: int
    totalItems: int
    totalPages: int


class ErrorResponse(BaseModel):
    """Respuesta de error estándar."""
    detail: str
