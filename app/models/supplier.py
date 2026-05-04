"""Schemas Pydantic para Supplier (Proveedor)."""

from pydantic import BaseModel


class SupplierBase(BaseModel):
    companyName: str
    contactName: str
    contactTitle: str
    city: str
    country: str
    phone: str
    fax: str | None = None


class SupplierCreate(SupplierBase):
    """Body para crear un proveedor."""
    pass


class SupplierUpdate(BaseModel):
    """Body para actualización parcial de proveedor."""
    companyName: str | None = None
    contactName: str | None = None
    contactTitle: str | None = None
    city: str | None = None
    country: str | None = None
    phone: str | None = None
    fax: str | None = None


class SupplierResponse(SupplierBase):
    """Respuesta de proveedor."""
    id: int

    model_config = {"from_attributes": True}
