"""Repositorio de acceso a datos para Order."""

from app.data.loader import db, next_id, next_order_number


def get_all() -> list[dict]:
    return list(db["orders"])


def get_by_id(order_id: int) -> dict | None:
    for o in db["orders"]:
        if o["id"] == order_id:
            return o
    return None


def get_by_customer_id(customer_id: int) -> list[dict]:
    return [o for o in db["orders"] if o["customerId"] == customer_id]


def create(data: dict) -> dict:
    data["id"] = next_id("order")
    data["orderNumber"] = next_order_number()
    db["orders"].append(data)
    return data


def update(order_id: int, data: dict) -> dict | None:
    order = get_by_id(order_id)
    if order:
        for key, value in data.items():
            if value is not None:
                order[key] = value
    return order


def delete(order_id: int) -> bool:
    order = get_by_id(order_id)
    if order:
        db["orders"].remove(order)
        # También eliminar los items asociados
        db["order_items"] = [
            i for i in db["order_items"] if i["orderId"] != order_id
        ]
        return True
    return False
