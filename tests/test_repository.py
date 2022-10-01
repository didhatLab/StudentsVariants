import pathlib

from unittest import TestCase
from easystore import SubStore, EasyStore

from src.repository import StudentRepository
from src.domain import Student


def create_test_student_store():
    store = EasyStore("test.estore")
    store.create_sub_store("students", ["id[pk]", "name", "surname", "patronymic"])
    students_store = store.get_sub_store("students")
    students_store.insert_one(name="dan", surname="sol", patronymic="kek")
    return store


def delete_test_files():
    pathlib.Path("test.estore").unlink()
    pathlib.Path("students.sbstore").unlink()
    pathlib.Path("students.sbstore.meta").unlink()


class TestStudentRepository(TestCase):

    def setUp(self) -> None:
        self.test_store = create_test_student_store()

    def tearDown(self) -> None:
        delete_test_files()

    def test_students_repo_common(self):
        students = StudentRepository(self.test_store)
        student = students.get_one()
        self.assertEqual("dan", student.name)
        self.assertEqual("sol", student.surname)
        self.assertEqual("kek", student.patronymic)
        self.assertEqual("1", student.student_id)

    def test_insert_into_repo(self):
        new_student = Student("max", "lol", "kol")
        students_repo = StudentRepository(self.test_store)
        res = students_repo.add_one(new_student)
        self.assertEqual(1, res)
        student = students_repo.get_one(name="max")
        self.assertEqual("max", student.name)
        self.assertEqual("lol", student.surname)
        self.assertEqual("kol", student.patronymic)
        self.assertEqual("2", student.student_id)

    def test_delete_one(self):
        students_repo = StudentRepository(self.test_store)
        res = students_repo.delete_one(name="dan")
        self.assertEqual(1, res)
        student = students_repo.get_one(name="dan")
        self.assertEqual(None, student)

    def test_get_many(self):
        students_repo = StudentRepository(self.test_store)
        students = students_repo.get_many()
        self.assertEqual(1, len(students))
        student = students[0]
        self.assertEqual("dan", student.name)
        self.assertEqual("sol", student.surname)
        self.assertEqual("1", student.student_id)

