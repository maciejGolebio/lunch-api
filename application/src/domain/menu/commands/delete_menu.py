from pydantic import BaseModel, Field

from domain.menu.entity.menu import MenuId


class DeleteMenuCommand(BaseModel):
    menu_id: MenuId


class DeleteMenuCommandResponse(BaseModel):
    menu_id: MenuId = Field(..., alias="menuId")

    class Config:
        allow_population_by_field_name = True
