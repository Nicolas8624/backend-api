import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """Caso 7: Verificar que la API está viva."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_swagger_docs():
    """Caso 8: Acceder a la documentación."""
    response = client.get("/api/v1/docs")
    assert response.status_code == 200
    assert "swagger-ui" in response.text.lower()

def test_list_orders_pagination():
    """Caso 6: Listar pedidos con paginación."""
    response = client.get("/api/v1/orders?page=1&limit=5")
    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) <= 5
    assert data["page"] == 1
    assert data["totalItems"] >= 10

def test_get_non_existent_order():
    """Caso 2: Consultar pedido inexistente."""
    response = client.get("/api/v1/orders/9999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

def test_create_order_recalculate():
    """Caso 1: Crear pedido válido y verificar totalAmount."""
    order_data = {
        "customerId": 1,
        "items": [
            {"productId": 1, "quantity": 2},
            {"productId": 2, "quantity": 1}
        ]
    }
    response = client.post("/api/v1/orders", json=order_data)
    assert response.status_code == 201
    res_data = response.json()
    # Total: 24.90*2 + 40.00*1 = 49.8 + 40 = 89.8
    assert res_data["totalAmount"] == 89.8
    assert res_data["orderNumber"].startswith("ORD-")

def test_order_item_lifecycle():
    """Casos 3, 4 y 5: Flujo de items y recálculo."""
    # 1. Crear pedido base
    order_res = client.post("/api/v1/orders", json={
        "customerId": 2,
        "items": [{"productId": 1, "quantity": 1}]
    }).json()
    order_id = order_res["id"]

    # 2. Agregar item (Caso 3)
    item_res = client.post(f"/api/v1/orders/{order_id}/items", json={
        "productId": 3, "quantity": 2
    })
    assert item_res.status_code == 201
    item_id = item_res.json()["id"]
    
    # 3. Actualizar cantidad (Caso 4)
    client.patch(f"/api/v1/orders/{order_id}/items/{item_id}", json={"quantity": 4})
    order_check = client.get(f"/api/v1/orders/{order_id}").json()
    # Total: 24.9(Prod 1) + 28.5*4(Prod 3) = 24.9 + 114 = 138.9
    assert order_check["totalAmount"] == 138.9

    # 4. Eliminar item (Caso 5)
    client.delete(f"/api/v1/orders/{order_id}/items/{item_id}")
    order_final = client.get(f"/api/v1/orders/{order_id}").json()
    assert order_final["totalAmount"] == 24.9
