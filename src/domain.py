from dataclasses import dataclass


class Student:

    def __init__(self, name, surname, patronymic, student_id=None):
        self.__student_id = student_id
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    @property
    def student_id(self):
        return self.__student_id

    def to_dict(self):
        if self.__student_id is None:
            return {
                "name": self.name,
                "surname": self.surname,
                "patronymic": self.patronymic
            }

        return {"id": self.__student_id,
                "name": self.name,
                "surname": self.surname,
                "patronymic": self.patronymic}


@dataclass
class Variant:
    variant_id: int
    file_path: str

    def to_dict(self):
        return {
            "id": self.variant_id,
            "path": self.file_path,
        }


@dataclass
class StudentWorkVariant:
    student_full_name: str
    variant_path: str

    def to_dict(self):
        return {
            "full_name": str(self.student_full_name),
            "path": str(self.variant_path),
        }
