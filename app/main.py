def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        return
    if command_parts[1] == command_parts[2]:
        return
    if command_parts[0] != "cp":
        return
    try:
        with (
            open(command_parts[1], "r") as source_file,
            open(command_parts[2], "w") as destination_file,
        ):
            destination_file.write(source_file.read())
    except Exception:
        pass
