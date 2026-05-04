"""Rutas para gestión de items dentro de un pedido."""

from fastapi import APIRouter, status
from app.services import order_item_service
from app.models.order_item import OrderItemCreate, OrderItemUpdate

router = APIRouter(prefix="/orders/{orderId}/items", tags=["Order Items"])


@router.get(
    "",
    summary="Listar items de un pedido",
)
async def list_items(orderId: int):
    return order_item_service.get_by_order_id(orderId)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Agregar un producto a un pedido (recalcula totalAmount)",
)
async def add_item(orderId: int, body: OrderItemCreate):
    return order_item_service.create(orderId, body.model_dump())


@router.patch(
    "/{itemId}",
    summary="Actualizar cantidad o precio unitario de un item (recalcula totalAmount)",
)
async def update_item(orderId: int, itemId: int, body: OrderItemUpdate):
    return order_item_service.update(orderId, itemId, body.model_dump(exclude_unset=True))


@router.delete(
    "/{itemId}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar un item del pedido (recalcula totalAmount)",
)
async def delete_item(orderId: int, itemId: int):
    order_item_service.delete(orderId, itemId)
    return None
