from bootsrap.container import get_mediator
from domain.order.commands.create_order import CreateOrderCommand, CreateOrderCommandResponse
from domain.order.queries.get_all_orders import GetAllOrdersQuery, GetAllOrdersQueryResponse
from domain.order.order_model import OrderId
from fastapi import APIRouter, Depends
from mediator.request import LocalRequestBus

router = APIRouter(tags=["orders"])


@router.post("/orders", status_code=200, response_model=CreateOrderCommandResponse)
async def create(create_order_command: CreateOrderCommand,
                 mediator: LocalRequestBus = Depends(get_mediator)) -> CreateOrderCommandResponse:
    return await mediator.execute(create_order_command)

@router.get("/orders", status_code=200, response_model=GetAllOrdersQueryResponse)
async def get_all(mediator: LocalRequestBus = Depends(get_mediator)) -> GetAllOrdersQueryResponse:
    return await mediator.execute(GetAllOrdersQuery())