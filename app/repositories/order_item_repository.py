"""Repositorio de acceso a datos para OrderItem."""

from app.data.loader import db, next_id


def get_by_order_id(order_id: int) -> list[dict]:
    return [i for i in db["order_items"] if i["orderId"] == order_id]


def get_by_id(item_id: int) -> dict | None:
    for i in db["order_items"]:
        if i["id"] == item_id:
            return i
    return None


def get_by_order_and_item(order_id: int, item_id: int) -> dict | None:
    for i in db["order_items"]:
        if i["orderId"] == order_id and i["id"] == item_id:
            return i
    return None


def create(data: dict) -> dict:
    data["id"] = next_id("order_item")
    db["order_items"].append(data)
    return data


def update(item_id: int, data: dict) -> dict | None:
    item = get_by_id(item_id)
    if item:
        for key, value in data.items():
            if value is not None:
                item[key] = value
    return item


def delete(item_id: int) -> bool:
    item = get_by_id(item_id)
    if item:
        db["order_items"].remove(item)
        return True
    return False


def delete_by_order_id(order_id: int):
    db["order_items"] = [
        i for i in db["order_items"] if i["orderId"] != order_id
    ]


def has_product_reference(product_id: int) -> bool:
    return any(i["productId"] == product_id for i in db["order_items"])
