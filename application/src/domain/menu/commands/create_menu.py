
from pydantic import BaseModel, Field

from domain.menu.entity.menu import Menu, MenuId


class CreateMenuCommand(BaseModel):
    menu: Menu


class CreateMenuCommandResponse(BaseModel):
    menu_id: MenuId = Field(..., alias="menuId")

    class Config:
        allow_population_by_field_name = True
