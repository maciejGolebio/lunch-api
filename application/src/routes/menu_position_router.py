from typing import List

from bootsrap.container import get_mediator

from domain.menu.commands.create_menu_position import CreateMenuPositionCommand, CreateMenuPositionCommandResponse
from domain.menu.commands.update_menu_position import UpdateMenuPositionCommand, UpdateMenuPositionCommandResponse
from domain.menu.commands.delete_menu_position import DeleteMenuPositionCommand, DeleteMenuPositionCommandResponse
from domain.menu.entity.menu import MenuId
from domain.menu.entity.menu_position import InputMenuPosition, MenuPositionId
from fastapi import APIRouter, Depends
from mediator.request import LocalRequestBus

router = APIRouter(tags=["menuPositions"])


@router.post("/menu/{menu_id}/position", status_code=200, response_model=CreateMenuPositionCommandResponse)
async def create(menu_id: MenuId,
                 menu_position: InputMenuPosition,
                 mediator: LocalRequestBus = Depends(get_mediator)) -> CreateMenuPositionCommandResponse:
    return await mediator.execute(CreateMenuPositionCommand(menu_id=menu_id, position=menu_position))


@router.put("/menu/{menu_id}/position/{menu_position_id}", status_code=200, response_model=UpdateMenuPositionCommandResponse)
async def update(menu_id: MenuId,
                 menu_position_id: MenuPositionId,
                 menu_position: InputMenuPosition,
                 mediator: LocalRequestBus = Depends(get_mediator)) -> UpdateMenuPositionCommandResponse:
    return await mediator.execute(
        UpdateMenuPositionCommand(
            menu_id=menu_id,
            position=menu_position,
            menu_position_id=menu_position_id
        )
    )


@router.delete(
    "/menu/{menu_id}/position/{menu_position_id}",
    status_code=200,
    response_model=DeleteMenuPositionCommandResponse)
async def delete(menu_id: MenuId,
                 menu_position_id: MenuPositionId,
                 mediator: LocalRequestBus = Depends(get_mediator)) -> DeleteMenuPositionCommandResponse:
    return await mediator.execute(
        DeleteMenuPositionCommand(
            menu_id=menu_id,
            menu_position_id=menu_position_id
        )
    )
