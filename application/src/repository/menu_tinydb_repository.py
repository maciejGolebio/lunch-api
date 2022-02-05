from typing import Callable, Mapping

from domain.menu.entity.menu import InputMenu, Menu, MenuId
from domain.menu.entity.menu_position import MenuPosition, MenuPositionId
from domain.menu.repository import menu_repository
from tinydb import Query

from repository.tinydb_base import TinyDBBase


class MenuTinyDBRepository(TinyDBBase, menu_repository.IMenuRepository):
    def __init__(self, client):
        super().__init__(client)

    def get_all(self):
        result = self.client.all()
        return [Menu.parse_obj(elem) for elem in result]

    def get_by_id(self, menu_id: MenuId):
        query = Query()
        # should retrun one elem list
        result = self.client.search(query.id == menu_id)
        if len(result) == 0:
            return None
        return Menu.parse_obj(result[0])

    def create(self, menu: Menu) -> None:
        self.client.insert(menu.dict())

    def update(self, menu_id: MenuId, menu: InputMenu) -> None:
        query = Query()
        self.client.update(menu.dict(), query.id == menu_id)

    def delete(self, menu_id: MenuId) -> None:
        query = Query()
        self.client.remove(query.menu_id == menu_id)

    def create_position(self, menu_id: MenuId, menu_position: MenuPosition) -> None:
        query = Query()
        self.client.update(
            self.__create_position_transform(menu_position),
            query.menu_id == menu_id
        )

    def update_position(self, menu_id: MenuId, menu_position: MenuPosition) -> None:
        query = Query()
        self.client.update(
            self.__update_position_transform(menu_position),
            query.menu_id == menu_id
        )

    def delete_position(self, menu_id: MenuId, menu_position_Id: MenuPositionId) -> None:
        query = Query()
        self.client.update(
            self.__delete_position_transform(menu_position_Id),
            query.menu_id == menu_id
        )

    @staticmethod
    def __create_position_transform(position: MenuPosition) -> Callable[[Mapping], None]:
        def transform(doc):
            menu = Menu.parse_obj(doc)
            menu.add_position(position)
            doc["positions"] = menu.dict().get("positions", [])

        return transform

    @staticmethod
    def __update_position_transform(position: MenuPosition) -> Callable[[Mapping], None]:
        def transform(doc):
            menu = Menu.parse_obj(doc)
            menu.update_position(position)
            doc["positions"] = menu.dict().get("positions", [])

        return transform

    @staticmethod
    def __delete_position_transform(menu_position_id: MenuPositionId) -> Callable[[Mapping], None]:
        def transform(doc):
            menu = Menu.parse_obj(doc)
            menu.delete_position(menu_position_id)
            doc["positions"] = menu.dict().get("positions", [])

        return transform
