def copy_file(command: str) -> None:
    if command in ["", " "] or command.count(" ") != 2:
        return None

    command, source_file_name, destination_file_name = command.split(" ")

    if command != "cp" or source_file_name == destination_file_name:
        return None

    try:
        with (
            open(source_file_name, "r") as file_in,
            open(destination_file_name, "w") as file_out,
        ):
            for line in file_in.readlines():
                file_out.write(line)
    except FileNotFoundError:
        return None
