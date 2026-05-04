"""Rutas para Products (Productos) — obligatorios + complementarios."""

from fastapi import APIRouter, Query, status
from app.services import product_service
from app.models.product import ProductCreate, ProductReplace, ProductUpdate

router = APIRouter(prefix="/products", tags=["Products"])


@router.get(
    "",
    summary="Listar productos con paginación y filtros",
)
async def list_products(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    supplierId: int = Query(None, description="Filtrar por proveedor"),
    search: str = Query(None, description="Buscar por nombre de producto"),
    discontinued: bool = Query(None, description="Filtrar por estado discontinuado"),
):
    return product_service.get_all(
        page=page, limit=limit, supplierId=supplierId,
        search=search, discontinued=discontinued,
    )


@router.get(
    "/{productId}",
    summary="Detalle de un producto con proveedor incluido",
)
async def get_product(productId: int):
    return product_service.get_by_id(productId)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo producto",
)
async def create_product(body: ProductCreate):
    return product_service.create(body.model_dump())


@router.put(
    "/{productId}",
    summary="Reemplazar un producto completamente",
)
async def replace_product(productId: int, body: ProductReplace):
    return product_service.replace(productId, body.model_dump())


@router.patch(
    "/{productId}",
    summary="Actualizar precio o estado discontinuado de un producto",
)
async def update_product(productId: int, body: ProductUpdate):
    return product_service.update(productId, body.model_dump(exclude_unset=True))


@router.delete(
    "/{productId}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Eliminar o marcar como discontinuado un producto",
)
async def delete_product(productId: int):
    product_service.delete(productId)
    return None
