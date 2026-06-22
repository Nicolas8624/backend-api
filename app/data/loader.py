"""Carga y normalización de datos desde Orders.json a memoria."""

import json
from pathlib import Path

EXTRA_CUSTOMERS_PATH = Path(__file__).parent.parent.parent / "customers_extra.json"

# Almacén de datos en memoria
db = {
    "suppliers": [],
    "products": [],
    "customers": [],
    "orders": [],
    "order_items": [],
    "counters": {
        "supplier_id": 0,
        "product_id": 0,
        "customer_id": 0,
        "order_id": 0,
        "order_item_id": 0,
        "order_number": 1000,
    },
}


def load_data():
    """Lee Orders.json y desnormaliza las entidades en listas separadas."""
    json_path = Path(__file__).parent.parent.parent / "Orders.json"
    with open(json_path, "r", encoding="utf-8") as f:
        raw_orders = json.load(f)

    suppliers_seen = set()
    products_seen = set()
    customers_seen = set()

    for raw_order in raw_orders:
        # --- Extraer Customer ---
        raw_customer = raw_order["customer"]
        if raw_customer["id"] not in customers_seen:
            customers_seen.add(raw_customer["id"])
            db["customers"].append({
                "id": raw_customer["id"],
                "firstName": raw_customer["firstName"],
                "lastName": raw_customer["lastName"],
                "city": raw_customer["city"],
                "country": raw_customer["country"],
                "phone": raw_customer["phone"],
            })

        # --- Extraer Items, Products y Suppliers ---
        for raw_item in raw_order["items"]:
            raw_product = raw_item["product"]
            raw_supplier = raw_product["supplier"]

            # Extraer Supplier
            if raw_supplier["id"] not in suppliers_seen:
                suppliers_seen.add(raw_supplier["id"])
                db["suppliers"].append({
                    "id": raw_supplier["id"],
                    "companyName": raw_supplier["companyName"],
                    "contactName": raw_supplier["contactName"],
                    "contactTitle": raw_supplier["contactTitle"],
                    "city": raw_supplier["city"],
                    "country": raw_supplier["country"],
                    "phone": raw_supplier["phone"],
                    "fax": raw_supplier.get("fax"),
                })

            # Extraer Product
            if raw_product["id"] not in products_seen:
                products_seen.add(raw_product["id"])
                db["products"].append({
                    "id": raw_product["id"],
                    "productName": raw_product["productName"],
                    "supplierId": raw_supplier["id"],
                    "unitPrice": raw_product["unitPrice"],
                    "package": raw_product["package"],
                    "isDiscontinued": raw_product["isDiscontinued"],
                })

            # Crear OrderItem
            db["order_items"].append({
                "id": raw_item["id"],
                "orderId": raw_order["id"],
                "productId": raw_product["id"],
                "unitPrice": raw_item["unitPrice"],
                "quantity": raw_item["quantity"],
            })

        # --- Crear Order ---
        db["orders"].append({
            "id": raw_order["id"],
            "orderNumber": raw_order["orderNumber"],
            "orderDate": raw_order["orderDate"],
            "customerId": raw_customer["id"],
            "totalAmount": raw_order["totalAmount"],
        })

    # --- Configurar contadores auto-incrementales ---
    if db["suppliers"]:
        db["counters"]["supplier_id"] = max(s["id"] for s in db["suppliers"])
    if db["products"]:
        db["counters"]["product_id"] = max(p["id"] for p in db["products"])
    if db["customers"]:
        db["counters"]["customer_id"] = max(c["id"] for c in db["customers"])
    if db["orders"]:
        db["counters"]["order_id"] = max(o["id"] for o in db["orders"])
    if db["order_items"]:
        db["counters"]["order_item_id"] = max(i["id"] for i in db["order_items"])
    if db["orders"]:
        max_num = max(
            int(o["orderNumber"].split("-")[1]) for o in db["orders"]
        )
        db["counters"]["order_number"] = max_num

    # --- Cargar clientes extra persistidos ---
    if EXTRA_CUSTOMERS_PATH.exists():
        with open(EXTRA_CUSTOMERS_PATH, "r", encoding="utf-8") as f:
            extra = json.load(f)
        existing_ids = {c["id"] for c in db["customers"]}
        for c in extra:
            if c["id"] not in existing_ids:
                db["customers"].append(c)
        if db["customers"]:
            db["counters"]["customer_id"] = max(c["id"] for c in db["customers"])


def next_id(entity: str) -> int:
    """Genera el siguiente ID auto-incremental para una entidad."""
    db["counters"][f"{entity}_id"] += 1
    return db["counters"][f"{entity}_id"]


def next_order_number() -> str:
    """Genera el siguiente número de orden (ORD-XXXX)."""
    db["counters"]["order_number"] += 1
    return f"ORD-{db['counters']['order_number']}"


def save_customers() -> None:
    """Persiste todos los clientes en customers_extra.json."""
    with open(EXTRA_CUSTOMERS_PATH, "w", encoding="utf-8") as f:
        json.dump(db["customers"], f, ensure_ascii=False, indent=2)
