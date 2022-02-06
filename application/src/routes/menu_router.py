from mediator.request import LocalRequestBus
from fastapi import APIRouter, Depends
from domain.menu.queries.get_menu_by_id import GetMenuByIdQuery, GetMenuByIdQueryResponse
from domain.menu.queries.get_all_menu_query import GetAllMenuQuery, GetAllMenuQueryResponse
from domain.menu.commands.delete_menu import DeleteMenuCommand, DeleteMenuCommandResponse
from domain.menu.commands.update_menu import UpdateMenuCommand, UpdateMenuCommandResponse
from domain.menu.commands.create_menu import CreateMenuCommand, CreateMenuCommandResponse
from dependency_injector.wiring import inject
from bootsrap.container import get_mediator
from typing import List

from domain.menu.entity.menu import Menu, MenuId, InputMenu


router = APIRouter(tags=["menu"])


@router.post("/menu", response_model=CreateMenuCommandResponse)
async def create(menu: InputMenu, mediator: LocalRequestBus = Depends(get_mediator)) -> CreateMenuCommandResponse:
    return await mediator.execute(CreateMenuCommand(menu=Menu(**menu.dict())))


@router.put("/menu/{menu_id}", response_model=UpdateMenuCommandResponse)
async def update_menu(menu_id: MenuId, menu: InputMenu, mediator: LocalRequestBus = Depends(get_mediator)) -> UpdateMenuCommandResponse:
    return await mediator.execute(UpdateMenuCommand(menu_id=menu_id, menu=menu))


@router.delete("/menu/{menu_id}", response_model=DeleteMenuCommandResponse)
async def delete_menu(menu_id: MenuId, mediator: LocalRequestBus = Depends(get_mediator)) -> DeleteMenuCommandResponse:
    return await mediator.execute(DeleteMenuCommand(menu_id=menu_id))


@router.get("/menu/{menu_id}", response_model=GetMenuByIdQueryResponse)
@inject
async def get(menu_id: MenuId, mediator: LocalRequestBus = Depends(get_mediator)) -> GetMenuByIdQueryResponse:
    return await mediator.execute(GetMenuByIdQuery(menu_id=menu_id))


@router.get("/menu", response_model=GetAllMenuQueryResponse)
@inject
async def get_all(mediator: LocalRequestBus = Depends(get_mediator)) -> GetAllMenuQueryResponse:
    return await mediator.execute(GetAllMenuQuery())
