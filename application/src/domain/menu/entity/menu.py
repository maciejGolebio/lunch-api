from unicodedata import name
from pydantic import BaseModel, Field
from typing import NewType
import uuid

MenuId = NewType('MenuId', str)


class Menu(BaseModel):
    id: MenuId = Field(default_factory=lambda: MenuId(str(uuid.uuid4())))
    name: str
    description: str


class InputMenu(BaseModel):
    name: str
    description: str
