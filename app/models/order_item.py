"""Schemas Pydantic para OrderItem (Ítem de pedido)."""

from pydantic import BaseModel, Field
from app.models.product import ProductDetailResponse


class OrderItemCreate(BaseModel):
    """Body para agregar un item a un pedido."""
    productId: int
    quantity: int = Field(..., gt=0, description="Cantidad mayor a 0")


class OrderItemUpdate(BaseModel):
    """Body para actualización parcial de item."""
    quantity: int | None = Field(None, gt=0)
    unitPrice: float | None = Field(None, gt=0)


class OrderItemResponse(BaseModel):
    """Respuesta de item con producto y proveedor incluidos."""
    id: int
    orderId: int
    productId: int
    unitPrice: float
    quantity: int
    product: ProductDetailResponse

    model_config = {"from_attributes": True}
