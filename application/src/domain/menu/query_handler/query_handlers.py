from typing import List
from domain.menu.entity.menu import Menu

from bootsrap.container import Container
from dependency_injector.wiring import Provide, inject
from domain.menu.queries.menu_queries import GetAllMenusQuery, GetMenuQuery
from domain.menu.repository.menu_repository import IMenuRepository


@inject
async def get_menu_query_handler(
        command: GetMenuQuery,
        repository: IMenuRepository = Provide[Container.menu_repository]) -> Menu:
    return repository.get_by_id(command.menu_id)
    
@inject
async def get_all_menus_query_handler(
    _: GetAllMenusQuery,
    repository: IMenuRepository = Provide[Container.menu_repository])->List[Menu]:
    return repository.get_all()

