def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3 or command_parts[0] != "cp":
        return

    _, source, target = command_parts
    if source == target:
        return

    try:
        with open(source, "r") as file_in, open(target, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
