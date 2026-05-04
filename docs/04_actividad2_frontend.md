# 04 — Actividad 2: Desarrollo Frontend

## Objetivo

Construir una interfaz web responsiva con **Next.js** y **Tailwind CSS** que consuma los endpoints de la Actividad 1. La aplicación debe permitir consultar, crear, editar y eliminar información del dominio `orders`, tanto en escritorio como en dispositivos móviles.

---

## Stack obligatorio

- **Framework:** Next.js (App Router)
- **Estilos:** Tailwind CSS
- **Consumo de API:** endpoints reales de la Actividad 1 (sin datos hardcodeados)

---

## Pantallas mínimas obligatorias

| Pantalla | Endpoints consumidos | Función esperada |
|---|---|---|
| **Dashboard** | `GET /api/v1/orders`, `GET /api/v1/products` | Resumen: total vendido, pedidos recientes, productos activos |
| **Listado de pedidos** | `GET /api/v1/orders` | Tabla con búsqueda, filtros por cliente/fecha y paginación |
| **Detalle de pedido** | `GET /api/v1/orders/{orderId}`, `GET /api/v1/orders/{orderId}/items` | Ver cliente, ítems, productos y total |
| **Crear pedido** | `POST /api/v1/orders`, `GET /api/v1/customers`, `GET /api/v1/products` | Formulario para seleccionar cliente y productos |
| **Editar pedido** | `PATCH /api/v1/orders/{orderId}`, `PATCH /api/v1/orders/{orderId}/items/{itemId}` | Modificar fecha, cliente o cantidades |
| **Gestión de productos** | `GET/POST/PATCH/DELETE /api/v1/products` | CRUD completo de productos y estado discontinuado |
| **Gestión de clientes** | `GET/POST/PATCH /api/v1/customers` | Administración básica de clientes |
| **Estado del sistema** | `GET /api/v1/health`, `GET /api/v1/docs` | Verificar API y enlazar documentación |

---

## Arquitectura sugerida (frontend)

```
Next.js App Router
    │
    ├── Pages / Routes
    │       │
    │       ├── Components (UI reutilizables)
    │       │       └── Tailwind UI
    │       │
    │       └── Hooks (estado y efectos)
    │
    └── Services / API Client
            │
            └── Types / Interfaces
                    │
                    ▼
              API REST (Actividad 1)
```

---

## Reglas importantes del frontend

1. **Cero datos hardcodeados:** si la API de la Actividad 1 ya está desplegada y operativa, la app debe consumir los endpoints reales.
2. **Diseño responsivo:** la interfaz debe funcionar correctamente en escritorio y móvil.
3. **Demo en vivo en sustentación:** deben demostrar al menos este flujo completo:
   - Listar pedidos
   - Crear un pedido nuevo
   - Editar un ítem
   - Verificar que el `totalAmount` se recalcula correctamente

---

## Entregables de la Actividad 2

- [ ] Aplicación Next.js + Tailwind desplegada con URL pública
- [ ] Consumo real de todos los endpoints de la Actividad 1
- [ ] Diseño responsivo (web y móvil)
- [ ] Repositorio GitHub con Gitflow y commits semánticos
- [ ] Informe técnico con: arquitectura frontend, componentes, integración API y evidencias
- [ ] Presentación y sustentación con demo funcional en vivo
- [ ] Archivo `README.md` en el repositorio con instrucciones de clonación, instalación y ejecución local

> ⚠️ **Sin README, la entrega NO será recibida.**
