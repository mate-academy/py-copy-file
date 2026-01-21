def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3:
        return

    command_name, source_file, destination_file = parts
    if command_name != "cp":
        return

    if source_file == destination_file:
        return

    try:
        with (open(source_file) as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
