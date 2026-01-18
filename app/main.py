def copy_file(command: str) -> None:
    parts = command.split()

    if parts[0] != "cp" or len(parts) != 3:
        return
    source_file, destination_file = parts[1], parts[2]

    try:
        if source_file == destination_file:
            return
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
