from typing import Callable, Mapping

from domain.order.order_model import Order, OrderId
from domain.order.repository import orders_repository
from tinydb import Query

from repository.tinydb_base import TinyDBBase


class OrdersTinyDBRepository(TinyDBBase, orders_repository.IOrdersRepository):
    def __init__(self, client):
        super().__init__(client)

    def get_all(self):
        result = self.client.all()
        return [Order.parse_obj(elem) for elem in result]

    def get_by_id(self, order_id: OrderId):
        query = Query()
        # should retrun one elem list
        result = self.client.search(query.order_id == order_id)
        if len(result) == 0:
            return None
        return Order.parse_obj(result[0])

    def create(self, order: Order) -> None:
        self.client.insert(order.dict())

    def update(self, order_id: OrderId, order: Order) -> None:
        query = Query()
        self.client.update(order.dict(), query.id == order_id)

    def delete(self, order_id: OrderId) -> None:
        query = Query()
        self.client.remove(query.id == order_id)

    def create_position(self, order_id: OrderId, menu_position) -> None:
        ...

    def update_position(self, order_id: OrderId, menu_position) -> None:
        ...

    def delete_position(self, order_id: OrderId, menu_position_Id) -> None:
        ...

    @staticmethod
    def __create_position_transform(position) -> Callable[[Mapping], None]:
        ...
