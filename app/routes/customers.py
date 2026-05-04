"""Rutas para Customers (Clientes) — complementarios."""

from fastapi import APIRouter, Query, status
from app.services import customer_service, order_service
from app.models.customer import CustomerCreate, CustomerUpdate

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.get(
    "",
    summary="Listar clientes con paginación y filtros",
)
async def list_customers(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    country: str = Query(None, description="Filtrar por país"),
    city: str = Query(None, description="Filtrar por ciudad"),
    search: str = Query(None, description="Buscar por nombre"),
):
    return customer_service.get_all(
        page=page, limit=limit, country=country, city=city, search=search,
    )


@router.get(
    "/{customerId}",
    summary="Detalle de un cliente",
)
async def get_customer(customerId: int):
    return customer_service.get_by_id(customerId)


@router.get(
    "/{customerId}/orders",
    summary="Pedidos de un cliente",
)
async def get_customer_orders(customerId: int):
    # Validar que el customer existe
    customer_service.get_by_id(customerId)
    return order_service.get_all(customerId=customerId)


@router.post(
    "",
    status_code=status.HTTP_201_CREATED,
    summary="Crear un nuevo cliente",
)
async def create_customer(body: CustomerCreate):
    return customer_service.create(body.model_dump())


@router.patch(
    "/{customerId}",
    summary="Actualizar un cliente parcialmente",
)
async def update_customer(customerId: int, body: CustomerUpdate):
    return customer_service.update(customerId, body.model_dump(exclude_unset=True))
