"""Servicio de lógica de negocio para Supplier."""

from app.repositories import supplier_repository
from app.errors.handlers import NotFoundError


def get_all(page: int = 1, limit: int = 10, country: str = None, search: str = None):
    suppliers = supplier_repository.get_all()

    if country:
        suppliers = [s for s in suppliers if s["country"].lower() == country.lower()]

    if search:
        q = search.lower()
        suppliers = [
            s for s in suppliers
            if q in s["companyName"].lower() or q in s["contactName"].lower()
        ]

    total_items = len(suppliers)
    total_pages = max(1, -(-total_items // limit))
    start = (page - 1) * limit

    return {
        "data": suppliers[start:start + limit],
        "page": page,
        "limit": limit,
        "totalItems": total_items,
        "totalPages": total_pages,
    }


def get_by_id(supplier_id: int):
    supplier = supplier_repository.get_by_id(supplier_id)
    if not supplier:
        raise NotFoundError(f"Supplier with id {supplier_id} not found")
    return supplier


def create(data: dict):
    return supplier_repository.create(data)


def update(supplier_id: int, data: dict):
    supplier = supplier_repository.get_by_id(supplier_id)
    if not supplier:
        raise NotFoundError(f"Supplier with id {supplier_id} not found")
    return supplier_repository.update(supplier_id, data)
