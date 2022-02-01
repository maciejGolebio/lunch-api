from repository.tinydb_base import TinyDBBase
from domain.menu.repository import menu_repository
from domain.menu.entity.menu import Menu, MenuId, InputMenu
from tinydb import Query
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


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

    def create(self, menu: Menu):
        self.client.insert(menu.dict())
        return menu.id

    def update(self, menu_id: MenuId, menu: InputMenu):
        query = Query()
        print(f"update menu {menu_id}, menu: {menu}")
        self.client.update(menu.dict(), query.id == menu_id)

    def delete(self, menu):
        self.client.remove(eids=[menu.id])
