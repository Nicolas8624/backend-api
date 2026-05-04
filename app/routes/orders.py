"""Rutas CRUD para Orders (Pedidos)."""

from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse
from app.services import order_service
from app.models.order import OrderCreate, OrderReplace, OrderPatch

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get(
    "",
    summary="Listar pedidos con paginación, filtros y ordenamiento",
)
async def list_orders(
    page: int = Query(1, ge=1, description="Número de página"),
    limit: int = Query(10, ge=1, le=100, description="Elementos por página"),
    customerId: int = Query(None, description="Filtrar por ID de cliente"),
    dateFrom: str = Query(None, description="Fecha desde (ISO 8601)"),
    dateTo: str = Query(None, description="Fecha hasta (ISO 8601)"),
    sort: str = Query(None, description="Ordenar por campo (ej: -orderDate, +totalAmount)"),
):
    return order_service.get_all(
        page=page, limit=limit, customerId=customerId,
        dateFrom=dateFrom, dateTo=dateTo, sort=sort,
    )


@router.get(
    "/{orderId}",
    summary="Detalle de un pedido (incluye cliente e items)",
)
async def get_order(orderId: int):
    return order_service.get_by_id(orderId)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo pedido",
)
async def create_order(body: OrderCreate):
    return order_service.create(body.model_dump())


@router.put(
    "/{orderId}",
    summary="Reemplazar completamente un pedido",
)
async def replace_order(orderId: int, body: OrderReplace):
    return order_service.replace(orderId, body.model_dump())


@router.patch(
    "/{orderId}",
    summary="Actualización parcial del pedido",
)
async def patch_order(orderId: int, body: OrderPatch):
    return order_service.patch(orderId, body.model_dump(exclude_unset=True))


@router.delete(
    "/{orderId}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un pedido",
)
async def delete_order(orderId: int):
    order_service.delete(orderId)
    return None
