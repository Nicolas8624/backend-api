"""Ruta de health check del sistema."""

from fastapi import APIRouter

router = APIRouter(tags=["Sistema"])


@router.get(
    "/health",
    summary="Verificar disponibilidad del servicio",
    response_description="Estado del servicio",
)
async def health_check():
    """Retorna el estado de salud de la API."""
    return {"status": "ok"}
