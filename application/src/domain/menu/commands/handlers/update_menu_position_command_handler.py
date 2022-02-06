from bootsrap.container import Container
from dependency_injector.wiring import Provide, inject
from domain.menu.commands.update_menu_position import UpdateMenuPositionCommand, UpdateMenuPositionCommandResponse
from domain.menu.entity.menu_position import MenuPosition
from domain.menu.repository.menu_repository import IMenuRepository


@inject
async def update_menu_position_command_handler(
        command: UpdateMenuPositionCommand,
        repository: IMenuRepository = Provide[Container.menu_repository]) -> UpdateMenuPositionCommandResponse:
    menu_position = MenuPosition(menu_position_id=command.menu_position_id,**command.position.dict())
    repository.update_position(command.menu_id, menu_position)
    return UpdateMenuPositionCommandResponse(menu_position_id=menu_position.menu_position_id)
