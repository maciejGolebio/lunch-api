from domain.menu.entity.menu import MenuId
from domain.order.order_model import OrderId
from domain.order.value_objects.payment import Payment
from pydantic import BaseModel, Field


class CreateOrderCommand(BaseModel):
    menu_id: MenuId
    payment: Payment


class CreateOrderCommandResponse(BaseModel):
    order_id: OrderId = Field(..., alias="orderId")

    class Config:
        allow_population_by_field_name = True
