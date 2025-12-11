def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    com, file_from, new_file = parts
    if file_from == new_file:
        return
    try:
        with (
            open(file_from, "r") as file_in,
            open(new_file, "w") as file_out
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
