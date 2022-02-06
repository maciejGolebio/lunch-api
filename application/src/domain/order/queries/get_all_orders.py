from typing import List

from domain.order.order_model import Order
from pydantic import BaseModel


class GetAllOrdersQuery(BaseModel):
    ...


class GetAllOrdersQueryResponse(BaseModel):
    orders: List[Order]
