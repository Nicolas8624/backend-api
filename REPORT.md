# Informe Técnico — Actividad 1: Backend API

## 1. Arquitectura del Sistema
Se ha implementado una arquitectura limpia por capas para asegurar la escalabilidad y mantenibilidad del código:

- **Capa de Rutas (Routes):** Define los endpoints y gestiona las peticiones HTTP.
- **Capa de Servicios (Services):** Contiene la lógica de negocio y reglas funcionales.
- **Capa de Repositorios (Repositories):** Encargada del acceso a los datos (en este caso, listas en memoria).
- **Capa de Datos (Data):** Gestiona la carga inicial y normalización del archivo `Orders.json`.
- **Modelos (Models):** Schemas de Pydantic para validación de datos y documentación OpenAPI.

## 2. Decisiones Técnicas
- **FastAPI:** Elegido por su alto rendimiento, validación automática con Pydantic y generación nativa de documentación Swagger.
- **Persistencia en Memoria:** Se optó por una estructura de diccionarios y listas para simular una base de datos, cumpliendo con los requerimientos de la actividad.
- **Normalización:** Los datos de `Orders.json` se normalizaron en 5 entidades (Customers, Products, Suppliers, Orders, Items) para facilitar las operaciones CRUD.

## 3. Reglas de Negocio Implementadas
- Recálculo automático del `totalAmount` en cada mutación de items.
- Generación de `orderNumber` incremental con formato `ORD-XXXX`.
- Validaciones de integridad referencial (existencia de cliente y producto antes de crear orden).
- Códigos de estado HTTP semánticos (200, 201, 204, 400, 404, 409).

## 4. Evidencias de Pruebas
Se ejecutaron pruebas automatizadas con `pytest` cubriendo los casos mínimos:

```bash
platform win32 -- Python 3.14.4, pytest-9.0.3
collected 6 items

tests\test_api.py ......                                                 [100%]
============================== 6 passed in 0.72s ==============================
```

**Casos validados:**
1. Creación de pedido con cálculo de total.
2. Consulta de pedidos inexistentes (404).
3. Ciclo de vida de items (Add/Update/Delete) con recálculo de total.
4. Paginación y filtros en listados.
5. Disponibilidad de Health Check y Swagger Docs.

## 5. Hitos Alcanzados
- [x] Estructura base y carga de datos.
- [x] CRUD completo de Orders e Items.
- [x] CRUD complementario de Customers, Products y Suppliers.
- [x] Documentación OpenAPI 100% funcional.
- [x] Cobertura de pruebas del 100% en casos obligatorios.
