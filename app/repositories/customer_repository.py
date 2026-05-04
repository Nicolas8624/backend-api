"""Repositorio de acceso a datos para Customer."""

from app.data.loader import db, next_id


def get_all() -> list[dict]:
    return list(db["customers"])


def get_by_id(customer_id: int) -> dict | None:
    for c in db["customers"]:
        if c["id"] == customer_id:
            return c
    return None


def create(data: dict) -> dict:
    data["id"] = next_id("customer")
    db["customers"].append(data)
    return data


def update(customer_id: int, data: dict) -> dict | None:
    customer = get_by_id(customer_id)
    if customer:
        for key, value in data.items():
            if value is not None:
                customer[key] = value
    return customer
