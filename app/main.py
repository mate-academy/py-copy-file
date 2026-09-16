def copy_file(command: str) -> None:
    parts: list[str] = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file: str = parts[1]
    destination_file: str = parts[2]

    if source_file == destination_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
