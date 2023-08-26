import shutil
import os


def copy_file(source_file: str, target_file: str) -> None:

    if source_file == target_file:
        return

    if not os.path.isfile(source_file):
        print(f"Source file '{source_file}' does not exist.")
        return

    shutil.copyfile(source_file, target_file)


copy_file("D:/All_For_Programming/Projects/py-copy-file/app/file.txt",
          "D:/All_For_Programming/Projects/py-copy-file/app/new_file.txt")
