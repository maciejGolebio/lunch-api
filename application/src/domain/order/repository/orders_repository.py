from abc import ABC, abstractmethod

class IOrdersRepository(ABC):

    @abstractmethod
    def get_all(self) -> None:
        """
            No limit not offset - basic example
        """

    @abstractmethod
    def get_by_id(self, order_id: int) -> None:
        """
            Get order by id
        """

    @abstractmethod
    def create(self, order: None) -> None:
        """
            Create new order
        """

    @abstractmethod
    def update(self, order: None) -> None:
        """
            Update order
        """

    @abstractmethod
    def delete(self, order_id: int) -> None:
        """
            Delete order
        """

    @abstractmethod
    def create_position(self, order_id: int, order_position: None) -> None:
        """
            Create new position in order
        """

    @abstractmethod
    def update_position(self, order_id: int, order_position: None) -> None:
        """
            Update position in order
        """

    @abstractmethod
    def delete_position(self, order_id: int, order_position_Id: int) -> None:
        """
            Delete position from order
        """