import random
from easystore import EasyStore

if __name__ == "__main__":
    store = EasyStore("../students_db/main.estore")

    store.create_sub_store("variants", ["variant_id[pk]", "file_path"])
    exam_store = store.get_sub_store("variants")
    paths_to_files = ["kek", "lol", "jojo",
                      "geg", "kick", "mom", "jj", "hdh",
                      "ddos", "kek", "jojo", "foo", "skd",
                      "foo", "jl", "bn", "ssd", "nn", "jojo"]
    number_variants = random.randint(20, 40)

    for number_var in range(number_variants):
        exam_store.insert_one(file_path=random.choice(paths_to_files))
