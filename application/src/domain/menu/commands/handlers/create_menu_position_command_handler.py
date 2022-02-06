from bootsrap.container import Container
from dependency_injector.wiring import Provide, inject
from domain.menu.commands.create_menu_position import CreateMenuPositionCommand, CreateMenuPositionCommandResponse
from domain.menu.entity.menu_position import MenuPosition
from domain.menu.repository.menu_repository import IMenuRepository


@inject
async def create_menu_position_command_handler(
        command: CreateMenuPositionCommand,
        repository: IMenuRepository = Provide[Container.menu_repository]) -> CreateMenuPositionCommandResponse:
    menu_position = MenuPosition(**command.position.dict())
    repository.create_position(command.menu_id, menu_position)
    return CreateMenuPositionCommandResponse(menu_position_id=menu_position.menu_position_id)
