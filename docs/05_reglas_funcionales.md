# 05 — Reglas Funcionales Obligatorias de la API

## Cálculo de totalAmount

```
totalAmount = Σ (unitPrice × quantity)  → para todos los ítems del pedido
```

Debe recalcularse automáticamente en estos tres eventos:
- Al **agregar** un ítem a un pedido
- Al **modificar** cantidad o precio de un ítem
- Al **eliminar** un ítem de un pedido

---

## Validaciones antes de crear un pedido

Antes de procesar un `POST /api/v1/orders`, validar:

1. El `customerId` enviado **existe** en la base de datos → si no: `404 Not Found`
2. Cada `productId` en el array `items` **existe** → si no: `400 Bad Request` o `404 Not Found`

---

## Códigos HTTP que deben usarse consistentemente

| Código | Cuándo usarlo |
|---|---|
| `200 OK` | Consulta o actualización exitosa |
| `201 Created` | Recurso creado exitosamente |
| `204 No Content` | Eliminación exitosa (sin cuerpo en la respuesta) |
| `400 Bad Request` | Datos inválidos o faltantes en el body |
| `404 Not Found` | El recurso solicitado no existe |
| `409 Conflict` | Conflicto (ej: producto con dependencias no se puede eliminar) |
| `500 Internal Server Error` | Error inesperado del servidor |

> Todos los errores deben incluir un **mensaje descriptivo** en el cuerpo de la respuesta.

---

## Documentación y monitoreo

- Exponer documentación OpenAPI/Swagger en `/api/v1/docs`
- Exponer endpoint de salud en `/api/v1/health` que retorne `{ "status": "ok" }`

---

## Versionamiento de rutas

Todas las rutas deben estar bajo el prefijo `/api/v1` para facilitar futuras evoluciones sin romper compatibilidad.
