# 02 — Contrato de Endpoints de la API

> **Prefijo de todas las rutas:** `/api/v1`  
> **Métodos HTTP válidos:** GET, POST, PUT, PATCH, DELETE  
> ⚠️ No existe ningún método llamado "PUTCH".

---

## ✅ Endpoints OBLIGATORIOS

### Orders (Pedidos)

| Método | Endpoint | Función | Entrada | Respuesta |
|---|---|---|---|---|
| GET | `/api/v1/orders` | Listar pedidos con paginación, filtros y ordenamiento | Query: `page`, `limit`, `customerId`, `dateFrom`, `dateTo`, `sort` | 200 OK: lista paginada |
| GET | `/api/v1/orders/{orderId}` | Detalle de un pedido (incluye cliente e items) | Path: `orderId` | 200 OK / 404 |
| POST | `/api/v1/orders` | Crear pedido (cliente + lista de productos) | Body: `customerId`, `items[{productId, quantity}]` | 201 Created |
| PUT | `/api/v1/orders/{orderId}` | Reemplazar completamente un pedido | Path + body completo | 200 OK / 400 / 404 |
| PATCH | `/api/v1/orders/{orderId}` | Actualización parcial del pedido | Body parcial: `orderDate`, `customerId`, `status` | 200 OK / 404 |
| DELETE | `/api/v1/orders/{orderId}` | Eliminar o anular un pedido | Path: `orderId` | 204 No Content / 404 |

### OrderItems (Ítems de pedido)

| Método | Endpoint | Función | Entrada | Respuesta |
|---|---|---|---|---|
| GET | `/api/v1/orders/{orderId}/items` | Listar items de un pedido | Path: `orderId` | 200 OK |
| POST | `/api/v1/orders/{orderId}/items` | Agregar producto a pedido (recalcula totalAmount) | Body: `productId`, `quantity` | 201 Created |
| PATCH | `/api/v1/orders/{orderId}/items/{itemId}` | Actualizar cantidad o precio unitario | Body parcial: `quantity`, `unitPrice` | 200 OK (recalcula total) |
| DELETE | `/api/v1/orders/{orderId}/items/{itemId}` | Eliminar item (recalcula totalAmount) | Path: `orderId`, `itemId` | 204 No Content |

### Products (Productos)

| Método | Endpoint | Función | Entrada | Respuesta |
|---|---|---|---|---|
| GET | `/api/v1/products` | Listar productos | Query: `page`, `limit`, `supplierId`, `search`, `discontinued` | 200 OK |
| GET | `/api/v1/products/{productId}` | Detalle de producto con proveedor | Path: `productId` | 200 OK / 404 |

### Sistema

| Método | Endpoint | Función | Respuesta |
|---|---|---|---|
| GET | `/api/v1/health` | Verificar disponibilidad del servicio | `200 OK: { status: "ok" }` |
| GET | `/api/v1/docs` | Documentación OpenAPI/Swagger | UI/documentación |

---

## ➕ Endpoints COMPLEMENTARIOS (opcionales pero valorados)

### Customers

| Método | Endpoint | Función |
|---|---|---|
| GET | `/api/v1/customers` | Listar clientes (page, limit, country, city, search) |
| GET | `/api/v1/customers/{customerId}` | Detalle de cliente |
| GET | `/api/v1/customers/{customerId}/orders` | Pedidos de un cliente |
| POST | `/api/v1/customers` | Crear cliente |
| PATCH | `/api/v1/customers/{customerId}` | Actualizar cliente parcialmente |

### Products (complementarios)

| Método | Endpoint | Función |
|---|---|---|
| POST | `/api/v1/products` | Crear producto |
| PUT | `/api/v1/products/{productId}` | Reemplazar producto completamente |
| PATCH | `/api/v1/products/{productId}` | Actualizar precio o estado discontinuado |
| DELETE | `/api/v1/products/{productId}` | Eliminar o marcar como discontinuado |

### Suppliers

| Método | Endpoint | Función |
|---|---|---|
| GET | `/api/v1/suppliers` | Listar proveedores (page, limit, country, search) |
| GET | `/api/v1/suppliers/{supplierId}` | Detalle de proveedor |
| GET | `/api/v1/suppliers/{supplierId}/products` | Productos de un proveedor |
| POST | `/api/v1/suppliers` | Crear proveedor |
| PATCH | `/api/v1/suppliers/{supplierId}` | Actualizar proveedor parcialmente |

---

## 📦 Ejemplos de Payloads

### POST `/api/v1/orders`
```json
{
  "customerId": 1,
  "items": [
    { "productId": 1, "quantity": 2 },
    { "productId": 3, "quantity": 1 }
  ]
}
```

### PATCH `/api/v1/orders/1/items/2`
```json
{
  "quantity": 5
}
```

### PATCH `/api/v1/products/4`
```json
{
  "unitPrice": 19.50,
  "isDiscontinued": false
}
```
