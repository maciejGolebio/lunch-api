from abc import ABC, abstractmethod

from domain.menu.entity.menu import Menu, MenuId
from domain.menu.entity.menu_position import MenuPosition, MenuPositionId


class IMenuRepository(ABC):

    @abstractmethod
    def get_all(self) -> Menu:
        """
            No limit not offset - basic example
        """

    @abstractmethod
    def get_by_id(self, menu_id: MenuId) -> Menu:
        """
            Get menu by id
        """

    @abstractmethod
    def create(self, menu: Menu) -> None:
        """
            Create new menu
        """

    @abstractmethod
    def update(self, menu: Menu) -> None:
        """
            Update menu
        """

    @abstractmethod
    def delete(self, menu_id: MenuId) -> None:
        """
            Delete menu
        """

    @abstractmethod
    def create_position(self, menu_id: MenuId, menu_position: MenuPosition) -> None:
        """
            Create new position in menu
        """

    @abstractmethod
    def update_position(self, menu_id: MenuId, menu_position: MenuPosition) -> None:
        """
            Update position in menu
        """

    @abstractmethod
    def delete_position(self, menu_id: MenuId, menu_position_Id: MenuPositionId) -> None:
        """
            Delete position from menu
        """
