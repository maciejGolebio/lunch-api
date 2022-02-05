from typing import List

from bootsrap.container import get_mediator
from dependency_injector.wiring import inject
from domain.menu.commands.menu_position_commands import \
    CreateMenuPositionCommand
from domain.menu.entity.menu import MenuId
from domain.menu.entity.menu_position import InputMenuPosition
from fastapi import APIRouter, Depends
from mediator.request import LocalRequestBus

router = APIRouter(tags=["menuPositions"])


@router.post("/menu/{menu_id}/position", response_model=None)
@inject
async def create(menu_id: MenuId, menu_position: InputMenuPosition, mediator: LocalRequestBus = Depends(get_mediator)) -> MenuId:
    return await mediator.execute(CreateMenuPositionCommand(menu_id=menu_id, position=menu_position))
