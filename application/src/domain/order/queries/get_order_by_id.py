from domain.order.order_model import Order, OrderId
from pydantic import BaseModel


class GetOrderByIdQuery(BaseModel):
    order_id: OrderId


class GetOrderByIdQueryResponse(BaseModel):
    order: Order
