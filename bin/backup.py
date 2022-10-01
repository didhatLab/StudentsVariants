import pathlib


def copy_file_to_backup(path_to_file: pathlib.Path):
    backup_file = pathlib.Path(f"../backup/{path_to_file.name}")
    with path_to_file.open(mode="r") as orig:
        with backup_file.open(mode="w") as new:
            string_from_original_file = orig.readline()
            while string_from_original_file:
                new.write(string_from_original_file)
                string_from_original_file = orig.readline()


if __name__ == "__main__":
    need_files_suffix = [".sbstore", ".estore", ".meta"]

    data_folder = pathlib.Path("../students_db")
    data_folder_files = [file for file in data_folder.iterdir()
                         if file.suffix in need_files_suffix]

    for file_path in data_folder_files:
        copy_file_to_backup(file_path)
