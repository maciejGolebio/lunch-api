from pydantic import BaseModel

from domain.menu.entity.menu import MenuId


class GetMenuQuery(BaseModel):
    menu_id: MenuId


class GetAllMenusQuery(BaseModel):
    ...
