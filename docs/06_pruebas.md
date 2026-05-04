# 06 — Pruebas Mínimas Esperadas

Estos son los casos de prueba que deben funcionar correctamente para la evaluación.

| # | Caso de prueba | Endpoint | Resultado esperado |
|---|---|---|---|
| 1 | Crear pedido válido | `POST /api/v1/orders` | `201 Created` y `totalAmount` calculado correctamente |
| 2 | Consultar pedido inexistente | `GET /api/v1/orders/9999` | `404 Not Found` |
| 3 | Agregar ítem a un pedido | `POST /api/v1/orders/{id}/items` | `201 Created` y `totalAmount` recalculado |
| 4 | Actualizar cantidad de un ítem | `PATCH /api/v1/orders/{id}/items/{itemId}` | `200 OK` y `totalAmount` recalculado |
| 5 | Eliminar un ítem | `DELETE /api/v1/orders/{id}/items/{itemId}` | `204 No Content` y total recalculado |
| 6 | Listar pedidos con paginación | `GET /api/v1/orders?page=1&limit=10` | `200 OK` con metadata de paginación |
| 7 | Verificar que la API está viva | `GET /api/v1/health` | `200 OK: { "status": "ok" }` |
| 8 | Acceder a la documentación | `GET /api/v1/docs` | Documentación Swagger/OpenAPI disponible |

---

## Flujo completo de demo (requerido en sustentación)

Deben demostrar en vivo este flujo sin errores:

1. `GET /api/v1/orders` → listar pedidos existentes
2. `POST /api/v1/orders` → crear un pedido nuevo con al menos 2 ítems
3. `GET /api/v1/orders/{orderId}` → verificar que el pedido fue creado correctamente
4. `PATCH /api/v1/orders/{orderId}/items/{itemId}` → editar la cantidad de un ítem
5. Verificar que el `totalAmount` cambió correctamente

---

## Herramientas sugeridas para pruebas

- **Postman** o **Insomnia** para pruebas manuales de la API
- **Swagger UI** (en `/api/v1/docs`) para pruebas desde el navegador
- **pytest** (Grupo A - Python) o **Jest/Supertest** (Grupo B - Node.js) para pruebas automatizadas
