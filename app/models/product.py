"""Schemas Pydantic para Product (Producto)."""

from pydantic import BaseModel
from app.models.supplier import SupplierResponse


class ProductBase(BaseModel):
    productName: str
    unitPrice: float
    package: str
    isDiscontinued: bool = False
    supplierId: int


class ProductCreate(ProductBase):
    """Body para crear un producto."""
    pass


class ProductReplace(ProductBase):
    """Body para reemplazar un producto completo (PUT)."""
    pass


class ProductUpdate(BaseModel):
    """Body para actualización parcial de producto."""
    productName: str | None = None
    unitPrice: float | None = None
    package: str | None = None
    isDiscontinued: bool | None = None
    supplierId: int | None = None


class ProductResponse(BaseModel):
    """Respuesta de producto (sin supplier anidado)."""
    id: int
    productName: str
    unitPrice: float
    package: str
    isDiscontinued: bool
    supplierId: int

    model_config = {"from_attributes": True}


class ProductDetailResponse(ProductResponse):
    """Respuesta de producto con proveedor incluido."""
    supplier: SupplierResponse
