import os


def copy_file(command: str) -> None:
    command_string = command.split()
    checker = os.path.isfile(command_string[1])
    if checker and command_string[1] != command_string[2]:
        with open(command_string[1], "r") as file_for_copy:
            text_from_file = file_for_copy.read()
        with open(command_string[2], "w") as copied_file:
            copied_file.write(text_from_file)
