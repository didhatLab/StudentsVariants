from abc import ABCMeta, abstractmethod
from typing import Union, List, Dict, Callable, Type
from easystore import EasyStore

from src.repository import StudentRepository, VariantsRepository, WorkRepository
from src.domain import Student, Variant
from src import commands
from src.commands import Command


class AbstractService(metaclass=ABCMeta):

    @abstractmethod
    def handle(self, command: commands.Command):
        raise NotImplementedError()


class StudentsService(AbstractService):

    def __init__(self, students_repo: StudentRepository):
        self.__student_repo = students_repo
        self.__handlers: Dict[Type[commands.Command], Callable] = {
            commands.GetAllStudents: self.get_all_students
        }

    def handle(self, command: commands.Command):
        handler = self.__handlers.get(type(command))
        res = handler(command)
        return res

    def get_all_students(self, command: commands.GetAllStudents) -> List[Student]:
        students = self.__student_repo.get_many()
        return students


class VariantsService(AbstractService):

    def __init__(self, variant_repo: VariantsRepository):
        self.__repo = variant_repo
        self.__handlers: Dict[Type[commands.Command], Callable] = {
            commands.GetAllVariants: self.get_all_variants
        }

    def handle(self, command: commands.Command):
        handler = self.__handlers.get(type(command))
        res = handler(command)
        return res

    def get_all_variants(self, command: commands.GetAllVariants) -> List[Variant]:
        variants = self.__repo.get_many()
        return variants


class WorkService(AbstractService):

    def __init__(self, work_repo: WorkRepository):
        self.__repo = work_repo
        self.__handlers: Dict[Type[commands.Command], Callable] = {
            commands.GetWork: self.get_work,
            commands.GenerateWork: self.generate_work
        }

    def handle(self, command: commands.Command):
        handler = self.__handlers.get(type(command))
        res = handler(command)
        return res

    def get_work(self, command: commands.GetWork):
        self.__repo.change_exam(command.work_name)
        works = self.__repo.get_many()
        return works

    def generate_work(self, command: commands.GenerateWork):
        self.__repo.create_exam(command.work_name)
        self.__repo.change_exam(command.work_name)
        works = self.__repo.get_many()
        return works
