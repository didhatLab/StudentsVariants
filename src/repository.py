import abc

from typing import Optional, List
from easystore import EasyStore

from src.domain import Student, Variant, StudentWorkVariant


class AbstractRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_one(self, **conditions):
        raise NotImplementedError()

    @abc.abstractmethod
    def add_one(self, *args, **kwargs):
        raise NotImplementedError()


class StudentRepository(AbstractRepository):

    def __init__(self, sub_store: EasyStore):
        self.__sub_store = sub_store
        self.__student_sub_store = self.__sub_store.get_sub_store("students")

    def get_one(self, **conditions) -> Optional[Student]:
        student = self.__student_sub_store.get_one(**conditions)
        if student is None:
            return None
        return Student(student.name, student.surname, student.patronymic, student_id=student.id)

    def add_one(self, student: Student):
        res = self.__student_sub_store.insert_one(**student.to_dict())
        return res

    def delete_one(self, **conditions):
        res = self.__student_sub_store.delete_one(**conditions)
        return res

    def get_many(self, **conditions) -> List[Student]:
        students = self.__student_sub_store.get_many(**conditions)

        return [Student(student.name,
                        student.surname,
                        student.patronymic,
                        student_id=student.id) for student in students]


class VariantsRepository(AbstractRepository):

    def __init__(self, store: EasyStore):
        self.__sub_store = store
        self.__variants_store = store.get_sub_store("variants")

    def get_one(self, **conditions):
        variant = self.__variants_store.get_one(**conditions)
        if variant is None:
            return None
        return Variant(variant_id=variant.variant_id, file_path=variant.file_path)

    def get_many(self, **conditions):
        variants = self.__variants_store.get_many()

        return [Variant(variant_id=variant.variant_id,
                        file_path=variant.file_path) for variant in variants]

    def add_one(self, *args, **kwargs):
        raise NotImplementedError()


class WorkRepository(AbstractRepository):

    def __init__(self, store: EasyStore):
        self.__store = store
        self.__work_store = store.get_sub_store("exam")

    def change_exam(self, exam_name: str):
        self.__work_store = self.__store.get_sub_store(exam_name)

    def create_exam(self, exam_name: str):
        self.__store.create_sub_store(exam_name, ["student_id", "variant_id", "id[pk]"])
        students_repo = StudentRepository(self.__store)
        variants_repo = VariantsRepository(self.__store)
        exam_store = self.__store.get_sub_store(exam_name)
        students = students_repo.get_many()
        variants = variants_repo.get_many()
        num_var = len(variants)
        for number, student in enumerate(students):
            exam_store.insert_one(student_id=student.student_id,
                                  variant_id=variants[number % num_var].variant_id)
        return True

    def get_one(self, **conditions):
        raise NotImplementedError()

    def get_many(self) -> List[StudentWorkVariant]:
        student_works = self.__work_store.get_many()
        student_repo = StudentRepository(self.__store)
        variants_repo = VariantsRepository(self.__store)
        res: List[StudentWorkVariant] = []
        for work in student_works:
            student = student_repo.get_one(id=int(work.student_id))
            variant = variants_repo.get_one(variant_id=int(work.variant_id))
            student_full_name = f"{student.surname} {student.name}"
            student_work = StudentWorkVariant(student_full_name=student_full_name,
                                              variant_path=variant.file_path)
            res.append(student_work)

        return res

    def add_one(self, *args, **kwargs):
        raise NotImplementedError()
