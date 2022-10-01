from easystore import EasyStore


def create_main_student_store(main_store: EasyStore):
    main_store.create_sub_store("students", ["id[pk]", "name", "surname", "patronymic"])


def create_variants_store(main_store: EasyStore):
    main_store.create_sub_store("variants", ["id[pk]", "path_to_file"])


if __name__ == "__main__":
    store = EasyStore("../students_db/main.estore")
    create_main_student_store(store)
    create_variants_store(store)
