"""
Orders API — Punto de entrada principal.

API REST de Órdenes de Compra desarrollada con FastAPI.
Programa ADSO — SENA.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.data.loader import load_data
from app.errors.handlers import (
    NotFoundError, BadRequestError, ConflictError,
    not_found_handler, bad_request_handler, conflict_handler,
)
from app.routes import health, orders, order_items, products, customers, suppliers

# --- Crear aplicación FastAPI ---
app = FastAPI(
    title="Orders API — SENA ADSO",
    description=(
        "API REST de Órdenes de Compra con CRUD completo de pedidos, "
        "items, productos, clientes y proveedores.\n\n"
        "**Programa:** Análisis y Desarrollo de Software — SENA\n\n"
        "**Versión:** 1.0.0"
    ),
    version="1.0.0",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
    openapi_url="/api/v1/openapi.json",
)

# --- CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Manejadores de excepciones ---
app.add_exception_handler(NotFoundError, not_found_handler)
app.add_exception_handler(BadRequestError, bad_request_handler)
app.add_exception_handler(ConflictError, conflict_handler)

# --- Cargar datos al iniciar ---
load_data()

# --- Registrar routers con prefijo /api/v1 ---
PREFIX = "/api/v1"

app.include_router(health.router, prefix=PREFIX)
app.include_router(orders.router, prefix=PREFIX)
app.include_router(order_items.router, prefix=PREFIX)
app.include_router(products.router, prefix=PREFIX)
app.include_router(customers.router, prefix=PREFIX)
app.include_router(suppliers.router, prefix=PREFIX)


@app.get("/", tags=["Root"], summary="Raíz de la API")
async def root():
    """Redirige a la documentación de la API."""
    return {
        "message": "Orders API v1.0.0",
        "docs": "/api/v1/docs",
        "health": "/api/v1/health",
    }
