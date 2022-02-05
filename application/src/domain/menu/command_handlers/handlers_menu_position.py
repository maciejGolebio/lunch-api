from bootsrap.container import Container
from dependency_injector.wiring import Provide, inject
from domain.menu.commands.menu_position_commands import (
    CreateMenuPositionCommand, DeleteMenuPositionCommand,
    UpdateMenuPositionCommand)
from domain.menu.entity.menu_position import MenuPosition, MenuPositionId
from domain.menu.repository.menu_repository import IMenuRepository


@inject
async def create_menu_position_command_handler(
        command: CreateMenuPositionCommand,
        repository: IMenuRepository = Provide[Container.menu_repository]) -> MenuPositionId:
    menu_position = MenuPosition(**command.position.dict())
    repository.create_position(command.menu_id, menu_position)
    return menu_position.menu_position_id


@inject
async def update_menu_position_command_handler(
        command: UpdateMenuPositionCommand,
        repository: IMenuRepository = Provide[Container.menu_repository]) -> MenuPositionId:
    repository.update_position(command.menu_id, command.position)
    return command.menu_position_id


@inject
async def delete_menu_position_command_handler(
        command: DeleteMenuPositionCommand,
        repository: IMenuRepository = Provide[Container.menu_repository]) -> MenuPositionId:
    repository.delete_position(command.menu_id, command.position_id)
    return command.menu_position_id
