from fastapi import FastAPI
from typing import List

from bootsrap.container import Container, get_mediator
from bootsrap.register_handlers import discover_handlers

from routes import menu_router
from routes import menu_position_router
from routes import orders_router


def create_app() -> FastAPI:

    container = Container()

    bus = get_mediator()
    discover_handlers(bus, container)

    app = FastAPI()
    app.include_router(menu_router.router)
    app.include_router(menu_position_router.router)
    app.include_router(orders_router.router)

    return app


app = create_app()
