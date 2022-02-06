from inspect import getmembers, isfunction
from typing import List

import pkgutil


def get_functions(module):
    return getmembers(module, isfunction)


def filter_dunders(dir_result: List[str]) -> List[str]:
    return [elem for elem in dir_result if not elem.startswith("__")]


def filter_leave_only_handlers(dir_result: List[str]) -> List[str]:
    return [elem for elem in dir_result if not elem.startswith("__") and elem.endswith("_handler")]


def commands_path(command_file: str, domain: str):
    return f"domain.{domain}.commands.handlers.{command_file}"


def queries_path(query_file: str, domain: str):
    return f"domain.{domain}.queries.handlers.{query_file}"


def get_modules_from_package(path: str, from_list: List[str]) -> List[str]:
    module = __import__(path, fromlist=from_list)
    return [name for _, name, _ in pkgutil.iter_modules(module.__path__)]


def discover_handlers(bus, container) -> None:
    import domain
    domains = [elem for elem in dir(
        domain) if not elem.startswith("_")]

    for domain in domains:
        commands = get_modules_from_package(
            f"domain.{domain}.commands.handlers", [domain])
        queries = get_modules_from_package(
            f"domain.{domain}.queries.handlers", [domain])
        for command in commands:
            command_module = __import__(commands_path(
                command, domain), fromlist=[domain])
            container.wire(modules=[command_module])

            command_handlers = filter_leave_only_handlers(dir(command_module))
            for command_handler in command_handlers:
                handler_function = getattr(__import__(commands_path(
                    command, domain), fromlist=[domain]), command_handler)
                try:
                    bus.register(handler_function)
                    print(f"Registered command handler {command_handler}")
                except Exception as e:
                    print(
                        f"Failed registering command handler {command_handler} with exception {e}")

        for query in queries:
            query_file = __import__(queries_path(
                query, domain), fromlist=[domain])
            container.wire(modules=[query_file])

            query_handlers = filter_leave_only_handlers(dir(query_file))
            for query_handler in query_handlers:
                query_function = getattr(__import__(queries_path(
                    query, domain), fromlist=[domain]), query_handler)

                try:
                    bus.register(query_function)
                    print(f"Registered query handler {query_handler}")
                except Exception as e:
                    print(
                        f"Failed registering command handler {query_handler} with exception {e}")
