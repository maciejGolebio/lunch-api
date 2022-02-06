
from typing import List

from bootsrap.container import Container
from dependency_injector.wiring import Provide, inject
from domain.order.order_model import Order, OrderId
from domain.order.queries.get_all_orders import (GetAllOrdersQuery,
                                                 GetAllOrdersQueryResponse)
from domain.order.repository.orders_repository import IOrdersRepository


@inject
async def get_all_orders_query_handler(
        query: GetAllOrdersQuery,
        repository: IOrdersRepository = Provide[Container.orders_repository]
) -> GetAllOrdersQueryResponse:

    all_orders: List[Order] = repository.get_all()
    return GetAllOrdersQueryResponse(orders=all_orders)
