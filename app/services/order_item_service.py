"""Servicio de lógica de negocio para OrderItem."""

from app.repositories import order_item_repository, order_repository, product_repository, supplier_repository
from app.errors.handlers import NotFoundError, BadRequestError


def _recalculate_total(order_id: int):
    """Recalcula el totalAmount de un pedido a partir de sus items."""
    items = order_item_repository.get_by_order_id(order_id)
    total = sum(item["unitPrice"] * item["quantity"] for item in items)
    order = order_repository.get_by_id(order_id)
    if order:
        order["totalAmount"] = round(total, 2)


def _enrich_item(item: dict) -> dict:
    """Agrega el producto y proveedor anidados a un item."""
    product = product_repository.get_by_id(item["productId"])
    supplier = None
    if product:
        supplier = supplier_repository.get_by_id(product["supplierId"])
    return {
        **item,
        "product": {**(product or {}), "supplier": supplier} if product else None,
    }


def get_by_order_id(order_id: int):
    order = order_repository.get_by_id(order_id)
    if not order:
        raise NotFoundError(f"Order with id {order_id} not found")

    items = order_item_repository.get_by_order_id(order_id)
    return [_enrich_item(item) for item in items]


def create(order_id: int, data: dict):
    order = order_repository.get_by_id(order_id)
    if not order:
        raise NotFoundError(f"Order with id {order_id} not found")

    product = product_repository.get_by_id(data["productId"])
    if not product:
        raise BadRequestError(f"Product with id {data['productId']} not found")

    item_data = {
        "orderId": order_id,
        "productId": data["productId"],
        "unitPrice": product["unitPrice"],
        "quantity": data["quantity"],
    }

    item = order_item_repository.create(item_data)
    _recalculate_total(order_id)
    return _enrich_item(item)


def update(order_id: int, item_id: int, data: dict):
    order = order_repository.get_by_id(order_id)
    if not order:
        raise NotFoundError(f"Order with id {order_id} not found")

    item = order_item_repository.get_by_order_and_item(order_id, item_id)
    if not item:
        raise NotFoundError(f"Item with id {item_id} not found in order {order_id}")

    update_data = {}
    if data.get("quantity") is not None:
        update_data["quantity"] = data["quantity"]
    if data.get("unitPrice") is not None:
        update_data["unitPrice"] = data["unitPrice"]

    if update_data:
        order_item_repository.update(item_id, update_data)

    _recalculate_total(order_id)
    return _enrich_item(item)


def delete(order_id: int, item_id: int):
    order = order_repository.get_by_id(order_id)
    if not order:
        raise NotFoundError(f"Order with id {order_id} not found")

    item = order_item_repository.get_by_order_and_item(order_id, item_id)
    if not item:
        raise NotFoundError(f"Item with id {item_id} not found in order {order_id}")

    order_item_repository.delete(item_id)
    _recalculate_total(order_id)
