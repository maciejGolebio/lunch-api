from typing import List

from domain.menu.entity.menu import Menu, MenuId, InputMenu
from domain.menu.queries.menu_queries import (GetAllMenusQuery,
                                              GetMenuQuery)
from bootsrap.container import get_mediator
from dependency_injector.wiring import inject
from domain.menu.commands.menu_commands import CreateMenuCommand, DeleteMenuCommand, UpdateMenuCommand
from fastapi import APIRouter, Depends
from mediator.request import LocalRequestBus

router = APIRouter(tags=["menu"])


@router.post("/menu", response_model=None)
@inject
async def create(menu: InputMenu, mediator: LocalRequestBus = Depends(get_mediator)) -> MenuId:
    return await mediator.execute(CreateMenuCommand(menu=Menu(**menu.dict())))


@router.put("/menu/{menu_id}", response_model=Menu)
@inject
async def update_menu(menu_id: MenuId, menu: InputMenu, mediator: LocalRequestBus = Depends(get_mediator)) -> MenuId:
    return await mediator.execute(UpdateMenuCommand(menu_id=menu_id, menu=menu))


@router.delete("/menu/{menu_id}", response_model=None)
@inject
async def delete_menu(menu_id: MenuId, mediator: LocalRequestBus = Depends(get_mediator)) -> MenuId:
    return await mediator.execute(DeleteMenuCommand(menu_id=menu_id))


@router.get("/menu/{menu_id}", response_model=Menu)
@inject
async def get(menu_id: MenuId, mediator: LocalRequestBus = Depends(get_mediator)) -> Menu:
    return await mediator.execute(GetMenuQuery(menu_id=menu_id))


@router.get("/menu", response_model=List)
@inject
async def get_all(mediator: LocalRequestBus = Depends(get_mediator)) -> List[Menu]:
    return await mediator.execute(GetAllMenusQuery())
