import os


def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3:
        first_file = command_list[1]
        second_file = command_list[2]

        if (command_list[0] == "cp"
                and os.path.exists(first_file)
                and os.path.exists(first_file)
                and first_file != second_file):
            with (
                open(first_file, "r") as file,
                open(second_file, "w") as newfile
            ):
                newfile.write(file.read())
