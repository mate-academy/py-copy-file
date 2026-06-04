import os


def copy_file(command: str) -> None:
    if command == "":
        return
    command_parts = command.split()
    if len(command_parts) < 3:
        return
    old_file = command_parts[1]
    new_file = command_parts[2]
    if (old_file == new_file
            or command_parts[0] != "cp"
            or not os.path.exists(old_file)):
        return

    with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
