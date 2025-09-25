import os


def copy_file(command: str) -> None:
    list_of_commands = command.split()
    if (
            len(list_of_commands) == 3
            and list_of_commands[0] == "cp"
            and list_of_commands[1] != list_of_commands[2]
            and os.path.exists(list_of_commands[1])
    ):
        source_file_name = list_of_commands[1]
        destination_file_object = list_of_commands[2]
        with (
            open(source_file_name, "r") as file_to_copy,
            open(destination_file_object, "w") as copy_of_file
        ):
            copy_of_file.write(file_to_copy.read())
