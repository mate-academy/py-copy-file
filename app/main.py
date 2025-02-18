import shutil


def copy_file(string: str) -> None:
    command, file_name, file_name_copy = string.split(" ")
    with open(file_name, "r") as file_in, \
            open(file_name_copy, "w") as file_out:
        shutil.copyfileobj(file_in, file_out)
