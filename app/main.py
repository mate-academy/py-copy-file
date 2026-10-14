def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    action, source, destination = parts

    if action != "cp" or source == destination:
        return

    try:
        with (
            open(source, "rb") as file_in,
            open(destination, "wb") as file_out,
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
