from domain.menu.entity.menu import MenuId
from domain.menu.entity.menu_position import InputMenuPosition,  MenuPositionId
from pydantic import BaseModel


class CreateMenuPositionCommand(BaseModel):
    """"
        Create a position in a menu
        (also create's position - postion cant lives with menu)
    """
    menu_id: MenuId
    position: InputMenuPosition


class UpdateMenuPositionCommand(BaseModel):
    menu_id: MenuId
    menu_position_id: MenuPositionId
    position: InputMenuPosition


class DeleteMenuPositionCommand(BaseModel):
    """"
        Delete a position from a menu, 
        (also delete's position from system - postion cant lives with menu)
    """
    menu_id: MenuId
    menu_position_id: MenuPositionId
