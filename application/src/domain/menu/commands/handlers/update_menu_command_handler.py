from bootsrap.container import Container
from dependency_injector.wiring import Provide, inject
from domain.menu.commands.update_menu import (UpdateMenuCommand,
                                              UpdateMenuCommandResponse)
from domain.menu.repository.menu_repository import IMenuRepository


@inject
async def update_menu_command_handler(
        command: UpdateMenuCommand,
        repository: IMenuRepository = Provide[Container.menu_repository]) -> UpdateMenuCommandResponse:
    repository.update(command.menu_id, command.menu)
    return UpdateMenuCommandResponse(menu_id=command.menu_id)
