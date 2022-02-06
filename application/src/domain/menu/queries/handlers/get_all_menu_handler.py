from bootsrap.container import Container
from dependency_injector.wiring import Provide, inject
from domain.menu.queries.get_all_menu_query import GetAllMenuQuery, GetAllMenuQueryResponse
from domain.menu.repository.menu_repository import IMenuRepository


@inject
async def get_all_menus_query_handler(
        _: GetAllMenuQuery,
        repository: IMenuRepository = Provide[Container.menu_repository]) -> GetAllMenuQueryResponse:
    return GetAllMenuQueryResponse(menus=repository.get_all())
