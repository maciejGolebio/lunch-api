from bootsrap.container import Container
from dependency_injector.wiring import Provide, inject
from domain.menu.commands.delete_menu import (DeleteMenuCommand,
                                              DeleteMenuCommandResponse)
from domain.menu.repository.menu_repository import IMenuRepository


@inject
async def delete_menu_command_handler(
        command: DeleteMenuCommand,
        repository: IMenuRepository = Provide[Container.menu_repository]) -> DeleteMenuCommandResponse:
    repository.delete(command.menu_id)
    return DeleteMenuCommandResponse(menu_id=command.menu_id)
