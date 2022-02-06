from fastapi import FastAPI
from typing import List

from bootsrap.container import Container, get_mediator
from bootsrap.register_handlers import discover_handlers
from domain.menu.command_handlers import handlers_menu_position
# from domain.menu.query_handler import query_handlers

from routes import menu_router
from routes import menu_position_router
from routes import orders_router


def create_app() -> FastAPI:

    container = Container()

    container.wire(modules=[handlers_menu_position])

    bus = get_mediator()
    discover_handlers(bus, container)

    bus.register(handlers_menu_position.create_menu_position_command_handler)
    bus.register(handlers_menu_position.update_menu_position_command_handler)
    bus.register(handlers_menu_position.delete_menu_position_command_handler)

    app = FastAPI()
    app.include_router(menu_router.router)
    app.include_router(menu_position_router.router)
    app.include_router(orders_router.router)

    return app


app = create_app()
