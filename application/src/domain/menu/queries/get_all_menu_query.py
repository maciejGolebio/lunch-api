from typing import List
from pydantic import BaseModel

from domain.menu.entity.menu import Menu


class GetAllMenuQuery(BaseModel):
    ...


class GetAllMenuQueryResponse(BaseModel):
    menus: List[Menu]
