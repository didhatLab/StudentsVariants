import abc

from dataclasses import dataclass


class Command(metaclass=abc.ABCMeta):
    pass


@dataclass(frozen=True)
class GetAllStudents(Command):
    pass


@dataclass(frozen=True)
class GetAllVariants(Command):
    pass


@dataclass(frozen=True)
class GetWork(Command):
    work_name: str


@dataclass(frozen=True)
class GenerateWork(Command):
    work_name: str
