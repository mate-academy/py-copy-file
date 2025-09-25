import os


def copy_file(command: str) -> None:
    list_of_commands = command.split(" ")
    if (
            list_of_commands[0] == "cp"
            and len(list_of_commands) == 3
            and os.path.exists(list_of_commands[1])
    ):
        with (
            open(list_of_commands[1], "r") as file_to_copy,
            open(list_of_commands[2], "w") as copy_of_file
        ):
            copy_of_file.write(file_to_copy.read())
