from pydantic import BaseModel

from domain.menu.entity.menu import Menu, MenuId, InputMenu


class CreateMenuCommand(BaseModel):
    menu: Menu


class UpdateMenuCommand(BaseModel):
    menu_id: MenuId
    menu: InputMenu


class DeleteMenuCommand(BaseModel):
    menu_id: MenuId
