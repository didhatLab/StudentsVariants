from easystore import EasyStore

from src import commands, repository, services


class CommandHandler:

    def __init__(self, injected_services):
        self.__services = injected_services

    def handle_command(self, command: commands.Command):
        handler = self.__services.get(type(command))
        return handler.handle(command)


def bootstrap() -> CommandHandler:
    store = EasyStore("../students_db/main.estore")
    injected_services = create_injected_services(store)

    command_handler = CommandHandler(injected_services)

    return command_handler


def create_injected_services(store: EasyStore):
    students_repo = repository.StudentRepository(store)
    variant_repo = repository.VariantsRepository(store)
    work_repo = repository.WorkRepository(store)
    injected_services = {
        commands.GetAllStudents: services.StudentsService(students_repo),
        commands.GetAllVariants: services.VariantsService(variant_repo),
        commands.GetWork: services.WorkService(work_repo),
        commands.GenerateWork: services.WorkService(work_repo),
    }
    return injected_services


