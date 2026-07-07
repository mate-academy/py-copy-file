def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    operation, source_file, destination_file = parts

    if operation != "cp":
        return

    if source_file == destination_file:
        return

    try:
        with open(source_file, "r", encoding="utf-8") as file_in, open(
            destination_file,
            "w",
            encoding="utf-8",
        ) as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
