from domain.menu.entity.menu import MenuId
from domain.menu.entity.menu_position import InputMenuPosition,  MenuPositionId
from pydantic import BaseModel, Field


class UpdateMenuPositionCommand(BaseModel):
    menu_id: MenuId
    menu_position_id: MenuPositionId
    position: InputMenuPosition


class UpdateMenuPositionCommandResponse(BaseModel):
    menu_position_id: MenuPositionId = Field(..., alias="menuPositionId")

    class Config:
        allow_population_by_field_name = True
