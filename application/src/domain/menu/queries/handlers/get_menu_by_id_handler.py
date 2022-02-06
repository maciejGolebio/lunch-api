from typing import List
from domain.menu.entity.menu import Menu

from bootsrap.container import Container
from dependency_injector.wiring import Provide, inject
from domain.menu.queries.get_menu_by_id import GetMenuByIdQuery, GetMenuByIdQueryResponse
from domain.menu.repository.menu_repository import IMenuRepository


@inject
async def get_menu_by_idquery_handler(
        command: GetMenuByIdQuery,
        repository: IMenuRepository = Provide[Container.menu_repository]) -> GetMenuByIdQueryResponse:
    return GetMenuByIdQueryResponse(menu=repository.get_by_id(command.menu_id))
