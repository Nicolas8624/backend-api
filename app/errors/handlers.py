"""Excepciones personalizadas y manejadores globales de errores."""

from fastapi import Request
from fastapi.responses import JSONResponse


class NotFoundError(Exception):
    """Recurso no encontrado (404)."""
    def __init__(self, detail: str = "Resource not found"):
        self.detail = detail


class BadRequestError(Exception):
    """Datos inválidos o faltantes (400)."""
    def __init__(self, detail: str = "Bad request"):
        self.detail = detail


class ConflictError(Exception):
    """Conflicto de dependencias (409)."""
    def __init__(self, detail: str = "Conflict"):
        self.detail = detail


async def not_found_handler(request: Request, exc: NotFoundError):
    return JSONResponse(status_code=404, content={"detail": exc.detail})


async def bad_request_handler(request: Request, exc: BadRequestError):
    return JSONResponse(status_code=400, content={"detail": exc.detail})


async def conflict_handler(request: Request, exc: ConflictError):
    return JSONResponse(status_code=409, content={"detail": exc.detail})


async def internal_error_handler(request: Request, exc: Exception):
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})
