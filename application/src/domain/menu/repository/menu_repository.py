from abc import ABC, abstractmethod

from domain.menu.entity.menu import Menu, MenuId


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
    def create(self, menu: Menu) -> Menu:
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
