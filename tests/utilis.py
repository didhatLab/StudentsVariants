import pathlib

from easystore import EasyStore


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
