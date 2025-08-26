def copy_file(command: str) -> None:
    command_parts = command.split(" ")

    if len(command_parts) < 3 or command_parts[0] != "cp":
        return

    file_to_copy = command_parts[1]
    file_to_create = command_parts[2]

    if file_to_copy == file_to_create:
        return

    try:
        with (
            open(file_to_copy, "r") as old_file,
            open(file_to_create, "w") as new_file
        ):
            new_file.write(old_file.read())
    except FileNotFoundError:
        return
