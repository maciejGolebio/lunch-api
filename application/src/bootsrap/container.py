from dependency_injector import containers, providers

from domain.menu.repository.menu_repository import IMenuRepository

from mediator.request import LocalRequestBus
from repository.menu_tinydb_repository import MenuTinyDBRepository
from tinydb import TinyDB

__mediator = None


def get_mediator()->LocalRequestBus:
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

    menu_repository: IMenuRepository = providers.Singleton(
        MenuTinyDBRepository,
        client=menu_db_client
    )
