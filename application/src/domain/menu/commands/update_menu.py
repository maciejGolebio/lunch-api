from pydantic import BaseModel, Field

from domain.menu.entity.menu import MenuId, InputMenu


class UpdateMenuCommand(BaseModel):
    menu_id: MenuId
    menu: InputMenu


class UpdateMenuCommandResponse(BaseModel):
    menu_id: MenuId = Field(..., alias="menuId")

    class Config:
        allow_population_by_field_name = True
