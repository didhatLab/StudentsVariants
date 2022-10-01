from easystore import EasyStore

if __name__ == "__main__":
    store = EasyStore("../students_db/main.estore")
    store.create_sub_store("exam", ["student_id", "variant_id", "id[pk]"])

    exam_store = store.get_sub_store("exam")
    students_store = store.get_sub_store("students")
    variant_store = store.get_sub_store("variants")

    students = students_store.get_many()
    variants = variant_store.get_many()
    len_variants = len(variants)

    for index, student in enumerate(students):
        exam_store.insert_one(student_id=student.id, variant_id=variants[index % len_variants].variant_id)


