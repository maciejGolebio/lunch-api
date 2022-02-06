import uuid
from typing import NewType

from domain.menu.entity.menu import Menu
from domain.order.value_objects.payment import Payment
from pydantic import BaseModel, Field


OrderId = NewType('OrderId', str)


class Order(BaseModel):
    order_id: OrderId = Field(
        default_factory=lambda: OrderId(str(uuid.uuid4())))
    menu: Menu
    payment: Payment

    @classmethod
    def create(cls, menu: Menu, payment: Payment) -> "Order":
        return cls(menu=menu, payment=payment)

    @property
    def total_price(self):
        return 0.00
