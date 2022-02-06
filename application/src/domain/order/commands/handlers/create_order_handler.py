from bootsrap.container import Container, get_mediator
from dependency_injector.wiring import Provide, inject
from domain.menu.queries.get_menu_by_id import GetMenuByIdQuery, GetMenuByIdQueryResponse
from domain.order.commands.create_order import (CreateOrderCommand,
                                                CreateOrderCommandResponse)
from domain.order.order_model import Order
from domain.order.repository.orders_repository import IOrdersRepository

# TODO: Domain errors
# TODO: Domain events


@inject
async def create_order_command_handler(
        command: CreateOrderCommand,
        repository: IOrdersRepository = Provide[Container.orders_repository],
        mediator=get_mediator()
) -> CreateOrderCommandResponse:

    response: GetMenuByIdQueryResponse = await mediator.execute(GetMenuByIdQuery(menu_id=command.menu_id))
    order = Order.create(menu=response.menu, payment=command.payment)
    repository.create(order)
    return CreateOrderCommandResponse(order_id=order.order_id)
