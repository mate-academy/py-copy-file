def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    action, file_from, file_to = parts

    if file_from == file_to:
        return

    try:
        with (
            open(file_from, "r") as file_in,
            open(file_to, "w") as file_out
        ):
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return
