# 🛒 Orders API — SENA ADSO

API REST de Órdenes de Compra desarrollada con **Python** y **FastAPI**.

> **Programa:** Análisis y Desarrollo de Software — SENA  
> **Centro:** Electricidad, Electrónica y Telecomunicaciones

---

## 📋 Descripción

API REST que gestiona órdenes de compra con las siguientes funcionalidades:

- **CRUD completo de pedidos** (Orders)
- **Gestión de items** dentro de cada pedido (OrderItems)
- **Consulta y gestión de productos** (Products)
- **Gestión de clientes** (Customers)
- **Gestión de proveedores** (Suppliers)
- **Health check** y **documentación Swagger/OpenAPI**
- Cálculo automático de `totalAmount` al modificar items
- Paginación, filtros y ordenamiento en listados
- Validaciones de negocio y códigos HTTP apropiados

---

## 🚀 Instalación y Ejecución Local

### Prerrequisitos
- Python 3.11 o superior

### 1. Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd backend-api
```

### 2. Crear entorno virtual
```bash
python -m venv env
```

### 3. Activar entorno virtual

**Windows:**
```bash
env\Scripts\activate
```

**Linux/Mac:**
```bash
source env/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 5. Ejecutar el servidor
```bash
uvicorn app.main:app --reload --port 8000
```

### 6. Acceder a la API
- **API Base:** http://localhost:8000
- **Swagger UI:** http://localhost:8000/api/v1/docs
- **ReDoc:** http://localhost:8000/api/v1/redoc
- **Health Check:** http://localhost:8000/api/v1/health

---

## 📂 Estructura del Proyecto

```
backend-api/
├── app/
│   ├── main.py              # Punto de entrada FastAPI
│   ├── data/
│   │   └── loader.py        # Carga y normalización de Orders.json
│   ├── models/              # Schemas Pydantic
│   │   ├── common.py        # Paginación y errores
│   │   ├── supplier.py
│   │   ├── product.py
│   │   ├── customer.py
│   │   ├── order_item.py
│   │   └── order.py
│   ├── repositories/        # Acceso a datos (CRUD en memoria)
│   │   ├── supplier_repository.py
│   │   ├── product_repository.py
│   │   ├── customer_repository.py
│   │   ├── order_repository.py
│   │   └── order_item_repository.py
│   ├── services/            # Lógica de negocio
│   │   ├── supplier_service.py
│   │   ├── product_service.py
│   │   ├── customer_service.py
│   │   ├── order_service.py
│   │   └── order_item_service.py
│   ├── routes/              # Endpoints HTTP
│   │   ├── health.py
│   │   ├── orders.py
│   │   ├── order_items.py
│   │   ├── products.py
│   │   ├── customers.py
│   │   └── suppliers.py
│   └── errors/
│       └── handlers.py      # Excepciones y manejadores
├── tests/                   # Pruebas automatizadas
├── Orders.json              # Datos fuente
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔗 Endpoints Principales

### Orders (Pedidos)
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/v1/orders` | Listar pedidos (paginación, filtros, ordenamiento) |
| GET | `/api/v1/orders/{id}` | Detalle de pedido |
| POST | `/api/v1/orders` | Crear pedido |
| PUT | `/api/v1/orders/{id}` | Reemplazar pedido |
| PATCH | `/api/v1/orders/{id}` | Actualizar pedido parcialmente |
| DELETE | `/api/v1/orders/{id}` | Eliminar pedido |

### Order Items
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/v1/orders/{id}/items` | Listar items |
| POST | `/api/v1/orders/{id}/items` | Agregar item |
| PATCH | `/api/v1/orders/{id}/items/{itemId}` | Actualizar item |
| DELETE | `/api/v1/orders/{id}/items/{itemId}` | Eliminar item |

### Products, Customers, Suppliers
Documentación completa disponible en `/api/v1/docs`.

---

## 🛠️ Stack Tecnológico

- **Python 3.11+**
- **FastAPI** — Framework web de alto rendimiento
- **Uvicorn** — Servidor ASGI
- **Pydantic v2** — Validación de datos
- **pytest** — Pruebas automatizadas

---

## 📄 Licencia

Proyecto académico — SENA ADSO 2026.
