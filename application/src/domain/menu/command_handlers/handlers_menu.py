from bootsrap.container import Container
from dependency_injector.wiring import Provide, inject
from domain.menu.commands.menu_commands import (CreateMenuCommand,
                                                DeleteMenuCommand,
                                                UpdateMenuCommand)
from domain.menu.entity.menu import MenuId
from domain.menu.repository.menu_repository import IMenuRepository


@inject
async def create_menu_command_handler(
        command: CreateMenuCommand,
        repository: IMenuRepository = Provide[Container.menu_repository]) -> MenuId:
    repository.create(command.menu)
    return command.menu.menu_id


@inject
async def update_menu_command_handler(
        command: UpdateMenuCommand,
        repository: IMenuRepository = Provide[Container.menu_repository]) -> MenuId:
    repository.update(command.menu_id, command.menu)
    return command.menu_id


@inject
async def delete_menu_command_handler(
        command: DeleteMenuCommand,
        repository: IMenuRepository = Provide[Container.menu_repository]) -> MenuId:
    repository.delete(command.menu_id)
    return command.menu_id
