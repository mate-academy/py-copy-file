def copy_file(command: str) -> None:

    source = command.split()
    if len(source) != 3 or source[0] != "cp":
        return

    source_filename = source[1]
    destination_filename = source[2]

    if source_filename == destination_filename:
        return
    try:
        with open(source_filename, "r") as file_in, open(destination_filename, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
