"""Schemas Pydantic para Order (Pedido)."""

from pydantic import BaseModel, Field
from app.models.customer import CustomerResponse
from app.models.order_item import OrderItemCreate, OrderItemResponse


class OrderCreate(BaseModel):
    """Body para crear un pedido."""
    customerId: int
    items: list[OrderItemCreate] = Field(..., min_length=1)


class OrderReplace(BaseModel):
    """Body para reemplazar un pedido completo (PUT)."""
    customerId: int
    items: list[OrderItemCreate] = Field(..., min_length=1)


class OrderPatch(BaseModel):
    """Body para actualización parcial del pedido."""
    orderDate: str | None = None
    customerId: int | None = None


class OrderResponse(BaseModel):
    """Respuesta completa de pedido con customer e items."""
    id: int
    orderNumber: str
    orderDate: str
    customerId: int
    totalAmount: float
    customer: CustomerResponse
    items: list[OrderItemResponse]

    model_config = {"from_attributes": True}


class OrderListItem(BaseModel):
    """Item de la lista de pedidos (sin items detallados)."""
    id: int
    orderNumber: str
    orderDate: str
    customerId: int
    totalAmount: float
    customer: CustomerResponse

    model_config = {"from_attributes": True}
