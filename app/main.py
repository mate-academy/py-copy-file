import os


def copy_file(command: str) -> str:
    elements = command.split(" ")
    copied_file = elements[-1]
    if command == "":
        return
    if elements[1] == elements[-1]:
        return
    if os.path.exists(elements[1]):
        if elements[0] == "cp":
            with (open(elements[1], "r") as file_to_copy,
                  open(copied_file, "w") as temp_file):
                temp_file.write(file_to_copy.read())
        return
