from bootsrap.container import Container
from dependency_injector.wiring import Provide, inject
from domain.menu.commands.create_menu import (
    CreateMenuCommand, CreateMenuCommandResponse)
from domain.menu.repository.menu_repository import IMenuRepository


@inject
async def create_menu_command_handler(
        command: CreateMenuCommand,
        repository: IMenuRepository = Provide[Container.menu_repository]) -> CreateMenuCommandResponse:
    repository.create(command.menu)
    return CreateMenuCommandResponse(menu_id=command.menu.menu_id)
