"""Schemas Pydantic para Customer (Cliente)."""

from pydantic import BaseModel


class CustomerBase(BaseModel):
    firstName: str
    lastName: str
    city: str
    country: str
    phone: str


class CustomerCreate(CustomerBase):
    """Body para crear un cliente."""
    pass


class CustomerUpdate(BaseModel):
    """Body para actualización parcial de cliente."""
    firstName: str | None = None
    lastName: str | None = None
    city: str | None = None
    country: str | None = None
    phone: str | None = None


class CustomerResponse(CustomerBase):
    """Respuesta de cliente."""
    id: int

    model_config = {"from_attributes": True}
