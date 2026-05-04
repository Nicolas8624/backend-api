# 03 — Actividad 1: Desarrollo de la API REST (Backend)

## Objetivo

Diseñar, construir, documentar, probar y desplegar una API REST sobre la colección `orders`, aplicando buenas prácticas de arquitectura por capas, Gitflow, Conventional Commits y SemVer.

---

## Stack tecnológico por grupo

| Grupo | Stack obligatorio | Recomendación |
|---|---|---|
| A | Python + Uvicorn + ambiente virtual `env` | FastAPI (integración natural con OpenAPI) |
| B | Node.js + Express | Separar rutas, controladores, servicios y repositorios |

---

## Endpoints mínimos a implementar

Para aprobar la actividad deben entregar como mínimo:

- CRUD completo de `orders`
- Gestión de items dentro de cada pedido
- Consultas básicas de `products` (listar y detalle)
- Endpoints de `health` y `docs`

> Implementar `customers` y `suppliers` no es obligatorio, pero **eleva la calidad** y habilita un frontend más robusto en la Actividad 2.

---

## Arquitectura sugerida (capas)

```
HTTP Client
    │
    ▼
Routes / Controllers
    │
    ├── Validators / Schemas
    │
    ▼
Services (lógica de negocio)
    │
    ▼
Repositories / Data Access
    │
    ▼
Data Source (JSON / BD)
    │
    └── Error Handler
    └── OpenAPI Docs
```

---

## Control de versiones — Gitflow

### Ramas requeridas
- `main` — versión estable y desplegada
- `develop` — integración de features
- `feature/*` — una rama por funcionalidad

### Commits semánticos (Conventional Commits)
```
feat: agregar endpoint GET /api/v1/orders
fix: corregir cálculo de totalAmount al eliminar item
docs: agregar descripción de endpoints en Swagger
test: agregar prueba para POST /api/v1/orders
refactor: separar lógica de orders en servicio propio
chore: configurar entorno virtual de Python
```

### Versionamiento semántico (SemVer)
- Primera versión estable: `v1.0.0`
- Parche (bugfix): `v1.0.1`
- Feature nueva sin romper compatibilidad: `v1.1.0`
- Cambio que rompe compatibilidad: `v2.0.0`

---

## Entregables de la Actividad 1

- [ ] Repositorio GitHub con Gitflow visible en ramas `main`, `develop` y `feature/*`
- [ ] Commits semánticos: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`
- [ ] Tag `v1.0.0` como primera versión estable
- [ ] API desplegada con URL funcional y pública
- [ ] Documentación Swagger/OpenAPI accesible en `/api/v1/docs`
- [ ] Informe técnico con: arquitectura, decisiones, hitos, pruebas y evidencias
- [ ] Presentación y sustentación técnica
- [ ] Archivo `README.md` en el repositorio con: descripción del proyecto, instrucciones de clonación, instalación y ejecución local

> ⚠️ **Sin README, la entrega NO será recibida.**
