from bootsrap.container import Container, get_mediator
from application.src.domain.menu.command_handlers import handlers_menu
from domain.menu.commands.menu_commands import CreateMenuCommand
from domain.menu.entity.menu import Menu


async def main(mediator):
    await mediator.execute(CreateMenuCommand(menu=Menu()))

if __name__ == "__main__":
    import asyncio
    
    bus = get_mediator()
    bus.register(handlers_menu.create_menu_command_handler)
    container = Container()

    container.wire(modules=[handlers_menu])
    container.config.arg.from_value("container argument")
    asyncio.run(main(bus))
