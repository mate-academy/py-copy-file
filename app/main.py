def copy_file(command: str) -> None:
    action, source, destination = command.split()

    if action != "cp" or source == destination:
        return

    with (
        open(source, "rb") as file_in,
        open(destination, "wb") as file_out,
    ):
        file_out.write(file_in.read())
