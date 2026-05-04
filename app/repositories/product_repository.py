"""Repositorio de acceso a datos para Product."""

from app.data.loader import db, next_id


def get_all() -> list[dict]:
    return list(db["products"])


def get_by_id(product_id: int) -> dict | None:
    for p in db["products"]:
        if p["id"] == product_id:
            return p
    return None


def get_by_supplier_id(supplier_id: int) -> list[dict]:
    return [p for p in db["products"] if p["supplierId"] == supplier_id]


def create(data: dict) -> dict:
    data["id"] = next_id("product")
    db["products"].append(data)
    return data


def update(product_id: int, data: dict) -> dict | None:
    product = get_by_id(product_id)
    if product:
        for key, value in data.items():
            if value is not None:
                product[key] = value
    return product


def delete(product_id: int) -> bool:
    product = get_by_id(product_id)
    if product:
        db["products"].remove(product)
        return True
    return False
