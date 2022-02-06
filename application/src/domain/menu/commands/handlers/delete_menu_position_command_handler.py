from bootsrap.container import Container
from dependency_injector.wiring import Provide, inject
from domain.menu.commands.delete_menu_position import DeleteMenuPositionCommand, DeleteMenuPositionCommandResponse
from domain.menu.entity.menu_position import MenuPosition
from domain.menu.repository.menu_repository import IMenuRepository


@inject
async def delete_menu_position_command_handler(
        command: DeleteMenuPositionCommand,
        repository: IMenuRepository = Provide[Container.menu_repository]) -> DeleteMenuPositionCommandResponse:
    repository.delete_position(command.menu_id, command.menu_position_id)
    return DeleteMenuPositionCommandResponse(menu_position_id=command.menu_position_id)
