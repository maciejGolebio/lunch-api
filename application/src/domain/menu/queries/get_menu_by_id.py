from pydantic import BaseModel

from domain.menu.entity.menu import MenuId, Menu


class GetMenuByIdQuery(BaseModel):
    menu_id: MenuId


class GetMenuByIdQueryResponse(BaseModel):
    menu: Menu
