"""Servicio de lógica de negocio para Order."""

from datetime import datetime, timezone
from app.repositories import (
    order_repository, customer_repository,
    product_repository, order_item_repository, supplier_repository,
)
from app.errors.handlers import NotFoundError, BadRequestError
from app.data.loader import next_order_number


def _enrich_item(item: dict) -> dict:
    """Agrega producto y proveedor a un item."""
    product = product_repository.get_by_id(item["productId"])
    supplier = None
    if product:
        supplier = supplier_repository.get_by_id(product["supplierId"])
    return {
        **item,
        "product": {**(product or {}), "supplier": supplier} if product else None,
    }


def _enrich_order(order: dict, include_items: bool = True) -> dict:
    """Agrega customer e items enriquecidos a un pedido."""
    customer = customer_repository.get_by_id(order["customerId"])
    result = {**order, "customer": customer}

    if include_items:
        items = order_item_repository.get_by_order_id(order["id"])
        result["items"] = [_enrich_item(item) for item in items]

    return result


def get_all(page: int = 1, limit: int = 10, customerId: int = None,
            dateFrom: str = None, dateTo: str = None, sort: str = None):
    orders = order_repository.get_all()

    # Filtrar por customerId
    if customerId is not None:
        orders = [o for o in orders if o["customerId"] == customerId]

    # Filtrar por rango de fechas
    if dateFrom:
        orders = [o for o in orders if o["orderDate"] >= dateFrom]
    if dateTo:
        orders = [o for o in orders if o["orderDate"] <= dateTo]

    # Ordenamiento
    if sort:
        reverse = sort.startswith("-")
        field = sort.lstrip("-+")
        if field in ("orderDate", "totalAmount", "orderNumber", "id"):
            orders = sorted(orders, key=lambda o: o.get(field, ""), reverse=reverse)

    total_items = len(orders)
    total_pages = max(1, -(-total_items // limit))
    start = (page - 1) * limit

    enriched = [_enrich_order(o, include_items=False) for o in orders[start:start + limit]]

    return {
        "data": enriched,
        "page": page,
        "limit": limit,
        "totalItems": total_items,
        "totalPages": total_pages,
    }


def get_by_id(order_id: int):
    order = order_repository.get_by_id(order_id)
    if not order:
        raise NotFoundError(f"Order with id {order_id} not found")
    return _enrich_order(order)


def create(data: dict):
    # Validar que el customer existe
    customer = customer_repository.get_by_id(data["customerId"])
    if not customer:
        raise NotFoundError(f"Customer with id {data['customerId']} not found")

    # Validar que todos los productos existen
    for item in data["items"]:
        product = product_repository.get_by_id(item["productId"])
        if not product:
            raise BadRequestError(f"Product with id {item['productId']} not found")

    # Crear la orden
    order_data = {
        "orderDate": datetime.now(timezone.utc).isoformat(),
        "customerId": data["customerId"],
        "totalAmount": 0.0,
    }
    order = order_repository.create(order_data)

    # Crear items y calcular total
    total = 0.0
    for item_data in data["items"]:
        product = product_repository.get_by_id(item_data["productId"])
        item = {
            "orderId": order["id"],
            "productId": item_data["productId"],
            "unitPrice": product["unitPrice"],
            "quantity": item_data["quantity"],
        }
        order_item_repository.create(item)
        total += product["unitPrice"] * item_data["quantity"]

    order["totalAmount"] = round(total, 2)
    return _enrich_order(order)


def replace(order_id: int, data: dict):
    order = order_repository.get_by_id(order_id)
    if not order:
        raise NotFoundError(f"Order with id {order_id} not found")

    # Validar customer
    customer = customer_repository.get_by_id(data["customerId"])
    if not customer:
        raise BadRequestError(f"Customer with id {data['customerId']} not found")

    # Validar productos
    for item in data["items"]:
        product = product_repository.get_by_id(item["productId"])
        if not product:
            raise BadRequestError(f"Product with id {item['productId']} not found")

    # Eliminar items anteriores
    order_item_repository.delete_by_order_id(order_id)

    # Actualizar orden
    order["customerId"] = data["customerId"]

    # Crear nuevos items
    total = 0.0
    for item_data in data["items"]:
        product = product_repository.get_by_id(item_data["productId"])
        item = {
            "orderId": order_id,
            "productId": item_data["productId"],
            "unitPrice": product["unitPrice"],
            "quantity": item_data["quantity"],
        }
        order_item_repository.create(item)
        total += product["unitPrice"] * item_data["quantity"]

    order["totalAmount"] = round(total, 2)
    return _enrich_order(order)


def patch(order_id: int, data: dict):
    order = order_repository.get_by_id(order_id)
    if not order:
        raise NotFoundError(f"Order with id {order_id} not found")

    if data.get("customerId") is not None:
        customer = customer_repository.get_by_id(data["customerId"])
        if not customer:
            raise NotFoundError(f"Customer with id {data['customerId']} not found")

    update_data = {}
    if data.get("orderDate") is not None:
        update_data["orderDate"] = data["orderDate"]
    if data.get("customerId") is not None:
        update_data["customerId"] = data["customerId"]

    if update_data:
        order_repository.update(order_id, update_data)

    return _enrich_order(order)


def delete(order_id: int):
    order = order_repository.get_by_id(order_id)
    if not order:
        raise NotFoundError(f"Order with id {order_id} not found")
    order_repository.delete(order_id)
