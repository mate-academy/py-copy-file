def copy_file(command: str) -> None:
    tokens = command.split(" ")
    if len(tokens) != 3:
        return

    command, source_file, destination_file = tokens

    if command != "cp" or source_file == destination_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())

    except FileNotFoundError:
        ...
