from pydantic import BaseModel, Field
from typing import List, NewType
import uuid

from domain.menu.entity.menu_position import MenuPosition, MenuPositionId

MenuId = NewType('MenuId', str)


class Menu(BaseModel):
    menu_id: MenuId = Field(default_factory=lambda: MenuId(str(uuid.uuid4())))
    name: str
    description: str
    positions: List[MenuPosition] = Field(default_factory=list)

    def add_position(self, position: MenuPosition):
        self.positions.append(position)

    def update_position(self, position: MenuPosition):
        self.positions = [p if p.menu_position_id !=
                          position.menu_position_id else position for p in self.positions]

    def delete_position(self, menu_position_id: MenuPositionId):
        self.positions = [
            p for p in self.positions if p.menu_position_id != menu_position_id
        ]


class InputMenu(BaseModel):
    name: str
    description: str
