import shutil


def copy_file(command: str) -> None:
    command, first_file, second_file = command.split(" ")
    if command == "cp" and first_file != second_file:
        with open(first_file, "r"), open(second_file, "w"):
            shutil.copy(first_file, second_file)
