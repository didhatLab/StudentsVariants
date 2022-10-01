import pathlib

from easystore import EasyStore
from dataclasses import dataclass
from typing import Iterable


@dataclass
class Student:
    name: str
    surname: str
    patronymic: str


def read_students_file(path_to_file) -> Iterable[Student]:
    file = pathlib.Path(path_to_file)
    with file.open(mode="r") as st:
        student_string = st.readline()
        while student_string:
            surname, name, patronymic = student_string.split()
            yield Student(name, surname, patronymic)
            student_string = st.readline()
    return


if __name__ == "__main__":
    store = EasyStore("../students_db/main.estore")

    students_store = store.get_sub_store("students")

    for student in read_students_file("names.txt"):
        students_store.insert_one(name=student.name, surname=student.surname,
                                  patronymic=student.patronymic)
