import os


def copy_file(command: str) -> None:
    list_of_names = command.split()
    if len(list_of_names) == 3 and list_of_names[0] == "cp":
        file_to_copy = list_of_names[1]
        copied_file = list_of_names[2]
        if file_to_copy == copied_file:
            return
        if os.path.exists(file_to_copy):
            with (open(file_to_copy, "rb") as file1,
                  open(copied_file, "wb") as file2):
                file2.write(file1.read())
