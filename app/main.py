def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    command, file_name, new_file_name = parts
    if command != "cp":
        return
    if file_name == new_file_name:
        return
    with (
        open(file_name, "r") as source,
        open(new_file_name, "w") as destination
    ):
        destination.write(source.read())
