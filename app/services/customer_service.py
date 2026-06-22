"""Servicio de lógica de negocio para Customer."""

from app.repositories import customer_repository
from app.errors.handlers import NotFoundError


def get_all(page: int = 1, limit: int = 10, country: str = None,
            city: str = None, search: str = None):
    customers = customer_repository.get_all()

    if country:
        customers = [c for c in customers if c["country"].lower() == country.lower()]

    if city:
        customers = [c for c in customers if c["city"].lower() == city.lower()]

    if search:
        q = search.lower()
        customers = [
            c for c in customers
            if q in c["firstName"].lower() or q in c["lastName"].lower()
        ]

    total_items = len(customers)
    total_pages = max(1, -(-total_items // limit))
    start = (page - 1) * limit

    return {
        "data": customers[start:start + limit],
        "page": page,
        "limit": limit,
        "totalItems": total_items,
        "totalPages": total_pages,
    }


def get_by_id(customer_id: int):
    customer = customer_repository.get_by_id(customer_id)
    if not customer:
        raise NotFoundError(f"Customer with id {customer_id} not found")
    return customer


def create(data: dict):
    return customer_repository.create(data)


def update(customer_id: int, data: dict):
    customer = customer_repository.get_by_id(customer_id)
    if not customer:
        raise NotFoundError(f"Customer with id {customer_id} not found")
    return customer_repository.update(customer_id, data)


def delete(customer_id: int):
    customer = customer_repository.get_by_id(customer_id)
    if not customer:
        raise NotFoundError(f"Customer with id {customer_id} not found")
    return customer_repository.delete(customer_id)
