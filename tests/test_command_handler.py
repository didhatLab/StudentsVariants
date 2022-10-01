from unittest import TestCase

from tests.utilis import create_test_student_store, delete_test_files
from src.bootstrap import CommandHandler, bootstrap, create_injected_services
from src import commands


class TestCommandHandler(TestCase):

    def setUp(self) -> None:
        self.store = create_test_student_store()
        injected_services = create_injected_services(self.store)
        self.command_handler = CommandHandler(injected_services)

    def tearDown(self) -> None:
        delete_test_files()

    def test_common(self):
        res = self.command_handler.handle_command(commands.GetAllStudents())
        self.assertEqual(1, len(res))
        student = res[0]
        self.assertEqual("dan", student.name)


