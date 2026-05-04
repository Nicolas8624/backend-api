"""Rutas para Suppliers (Proveedores) — complementarios."""

from fastapi import APIRouter, Query, status
from app.services import supplier_service, product_service
from app.models.supplier import SupplierCreate, SupplierUpdate
from app.repositories import product_repository

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])


@router.get(
    "",
    summary="Listar proveedores con paginación y filtros",
)
async def list_suppliers(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    country: str = Query(None, description="Filtrar por país"),
    search: str = Query(None, description="Buscar por nombre de empresa o contacto"),
):
    return supplier_service.get_all(
        page=page, limit=limit, country=country, search=search,
    )


@router.get(
    "/{supplierId}",
    summary="Detalle de un proveedor",
)
async def get_supplier(supplierId: int):
    return supplier_service.get_by_id(supplierId)


@router.get(
    "/{supplierId}/products",
    summary="Productos de un proveedor",
)
async def get_supplier_products(supplierId: int):
    # Validar que el supplier existe
    supplier_service.get_by_id(supplierId)
    products = product_repository.get_by_supplier_id(supplierId)
    return products


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo proveedor",
)
async def create_supplier(body: SupplierCreate):
    return supplier_service.create(body.model_dump())


@router.patch(
    "/{supplierId}",
    summary="Actualizar un proveedor parcialmente",
)
async def update_supplier(supplierId: int, body: SupplierUpdate):
    return supplier_service.update(supplierId, body.model_dump(exclude_unset=True))
