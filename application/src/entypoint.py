from fastapi import FastAPI

from bootsrap.container import Container, get_mediator
from domain.menu.command_handlers import command_handlers
from domain.menu.query_handler import query_handlers
from routes import menu_router


def create_app() -> FastAPI:
    container = Container()
    app = FastAPI()

    bus = get_mediator()
    bus.register(command_handlers.create_menu_command_handler)
    bus.register(command_handlers.update_menu_command_handler)
    bus.register(command_handlers.delete_menu_command_handler)
    bus.register(query_handlers.get_menu_query_handler)
    bus.register(query_handlers.get_all_menus_query_handler)

    app.container = container
    container.wire(modules=[command_handlers])
    container.wire(modules=[query_handlers])
    app.include_router(menu_router.router)
    return app


app = create_app()
