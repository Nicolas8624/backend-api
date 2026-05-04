"""Repositorio de acceso a datos para Supplier."""

from app.data.loader import db, next_id


def get_all() -> list[dict]:
    return list(db["suppliers"])


def get_by_id(supplier_id: int) -> dict | None:
    for s in db["suppliers"]:
        if s["id"] == supplier_id:
            return s
    return None


def create(data: dict) -> dict:
    data["id"] = next_id("supplier")
    db["suppliers"].append(data)
    return data


def update(supplier_id: int, data: dict) -> dict | None:
    supplier = get_by_id(supplier_id)
    if supplier:
        for key, value in data.items():
            if value is not None:
                supplier[key] = value
    return supplier
