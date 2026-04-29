import os


def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        return

    if command_parts[0] != "cp":
        return

    file_name = command_parts[1]
    new_file_name = command_parts[2]

    if file_name == new_file_name:
        return

    if not os.path.exists(file_name):
        return

    with open(file_name, "r") as file_in, open(new_file_name, "w") as file_out:
        file_out.write(file_in.read())
