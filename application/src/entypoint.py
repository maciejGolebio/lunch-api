from fastapi import FastAPI

from bootsrap.container import Container, get_mediator
from domain.menu.command_handlers import handlers_menu, handlers_menu_position
from domain.menu.query_handler import query_handlers

from routes import menu_router
from routes import menu_position_router


def create_app() -> FastAPI:
    container = Container()
    app = FastAPI()

    bus = get_mediator()
    bus.register(handlers_menu.create_menu_command_handler)
    bus.register(handlers_menu.update_menu_command_handler)
    bus.register(handlers_menu.delete_menu_command_handler)
    bus.register(handlers_menu_position.create_menu_position_command_handler)
    bus.register(handlers_menu_position.update_menu_position_command_handler)
    bus.register(handlers_menu_position.delete_menu_position_command_handler)

    bus.register(query_handlers.get_menu_query_handler)
    bus.register(query_handlers.get_all_menus_query_handler)

    app.container = container
    container.wire(modules=[handlers_menu])
    container.wire(modules=[handlers_menu_position])
    container.wire(modules=[query_handlers])

    app.include_router(menu_router.router)
    app.include_router(menu_position_router.router)
    return app


app = create_app()
