from domain.menu.entity.menu import MenuId
from domain.menu.entity.menu_position import InputMenuPosition, MenuPositionId
from pydantic import BaseModel, Field


class CreateMenuPositionCommand(BaseModel):
    """"
        Create a position in a menu
        (also create's position - postion cant lives with menu)
    """
    menu_id: MenuId
    position: InputMenuPosition

class CreateMenuPositionCommandResponse(BaseModel):
    menu_position_id: MenuPositionId = Field(..., alias="menuPositionId")
    class Config:
        allow_population_by_field_name = True
