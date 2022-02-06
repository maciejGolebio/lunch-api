from domain.menu.entity.menu import MenuId
from domain.menu.entity.menu_position import MenuPositionId
from pydantic import BaseModel, Field


class DeleteMenuPositionCommand(BaseModel):
    """"
        Delete a position from a menu, 
        (also delete's position from system - postion cant lives with menu)
    """
    menu_id: MenuId
    menu_position_id: MenuPositionId

class DeleteMenuPositionCommandResponse(BaseModel):
    menu_position_id: MenuPositionId = Field(..., alias="menuPositionId")

    class Config:
        allow_population_by_field_name = True