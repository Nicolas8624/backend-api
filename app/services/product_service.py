"""Servicio de lógica de negocio para Product."""

from app.repositories import product_repository, supplier_repository, order_item_repository
from app.errors.handlers import NotFoundError, ConflictError


def get_all(page: int = 1, limit: int = 10, supplierId: int = None,
            search: str = None, discontinued: bool = None):
    products = product_repository.get_all()

    if supplierId is not None:
        products = [p for p in products if p["supplierId"] == supplierId]

    if search:
        q = search.lower()
        products = [p for p in products if q in p["productName"].lower()]

    if discontinued is not None:
        products = [p for p in products if p["isDiscontinued"] == discontinued]

    total_items = len(products)
    total_pages = max(1, -(-total_items // limit))
    start = (page - 1) * limit

    return {
        "data": products[start:start + limit],
        "page": page,
        "limit": limit,
        "totalItems": total_items,
        "totalPages": total_pages,
    }


def get_by_id(product_id: int):
    product = product_repository.get_by_id(product_id)
    if not product:
        raise NotFoundError(f"Product with id {product_id} not found")

    supplier = supplier_repository.get_by_id(product["supplierId"])
    return {**product, "supplier": supplier}


def create(data: dict):
    supplier = supplier_repository.get_by_id(data["supplierId"])
    if not supplier:
        raise NotFoundError(f"Supplier with id {data['supplierId']} not found")
    return product_repository.create(data)


def replace(product_id: int, data: dict):
    product = product_repository.get_by_id(product_id)
    if not product:
        raise NotFoundError(f"Product with id {product_id} not found")

    supplier = supplier_repository.get_by_id(data["supplierId"])
    if not supplier:
        raise NotFoundError(f"Supplier with id {data['supplierId']} not found")

    for key in ["productName", "unitPrice", "package", "isDiscontinued", "supplierId"]:
        product[key] = data[key]
    return product


def update(product_id: int, data: dict):
    product = product_repository.get_by_id(product_id)
    if not product:
        raise NotFoundError(f"Product with id {product_id} not found")

    if "supplierId" in data and data["supplierId"] is not None:
        supplier = supplier_repository.get_by_id(data["supplierId"])
        if not supplier:
            raise NotFoundError(f"Supplier with id {data['supplierId']} not found")

    return product_repository.update(product_id, data)


def delete(product_id: int):
    product = product_repository.get_by_id(product_id)
    if not product:
        raise NotFoundError(f"Product with id {product_id} not found")

    if order_item_repository.has_product_reference(product_id):
        raise ConflictError(
            f"Product with id {product_id} cannot be deleted because it is referenced by order items"
        )

    product_repository.delete(product_id)
