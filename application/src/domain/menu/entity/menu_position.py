import uuid
from pydantic import BaseModel, Field
from typing import NewType
import decimal
MenuPositionId = NewType('MenuPositionId', str)


class InputMenuPosition(BaseModel):
    name: str
    description: str
    price: decimal.Decimal = Field(
        default_factory=lambda: 0.00, decimal_places=2, gt=0
    )


class MenuPosition(InputMenuPosition):
    menu_position_id: MenuPositionId = Field(
        default_factory=lambda: MenuPositionId(str(uuid.uuid4()))
    )
