def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    if parts[0] != "cp":
        return

    _, file_name, new_file_name = parts

    if file_name == new_file_name:
        return
    try:
        with (
            open(file_name, mode="r") as file,
            open(new_file_name, mode="w") as new_file
        ):
            content = file.read()
            new_file.write(content)

    except FileNotFoundError:
        return
