from bootsrap.container import Container, get_mediator
from domain.menu.command_handlers import command_handlers
from domain.menu.commands.menu_commands import CreateMenuCommand
from domain.menu.entity.menu import Menu


async def main(mediator):
    await mediator.execute(CreateMenuCommand(menu=Menu()))

if __name__ == "__main__":
    import asyncio
    
    bus = get_mediator()
    bus.register(command_handlers.create_menu_command_handler)
    container = Container()

    container.wire(modules=[command_handlers])
    container.config.arg.from_value("container argument")
    asyncio.run(main(bus))
