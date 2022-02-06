from dependency_injector import containers, providers

from domain.menu.repository.menu_repository import IMenuRepository
from domain.order.repository.orders_repository import IOrdersRepository
from mediator.request import LocalRequestBus
from repository.menu_tinydb_repository import MenuTinyDBRepository
from repository.order_tinydb_repository import OrdersTinyDBRepository
from tinydb import TinyDB

__mediator = None


def get_mediator() -> LocalRequestBus:
    global __mediator
    if __mediator is None:
        __mediator = LocalRequestBus()
    return __mediator


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    menu_db_client: TinyDB = providers.Resource(
        TinyDB,
        "menu.json"
    )
    order_db_client: TinyDB = providers.Resource(
        TinyDB,
        "order.json"
    )

    menu_repository: IMenuRepository = providers.Singleton(
        MenuTinyDBRepository,
        client=menu_db_client
    )

    orders_repository: IOrdersRepository = providers.Singleton(
        OrdersTinyDBRepository,
        client=order_db_client
    )
