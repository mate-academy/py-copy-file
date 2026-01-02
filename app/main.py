def copy_file(command: str):
    if command.count(" ") != 2:
        return

    tokens = command.split(" ")
    if tokens[0] != "cp":
        return

    source_file_name = tokens[1]
    destination_file_name = tokens[2]

    if source_file_name == destination_file_name:
        return

    try:
        with open(source_file_name, "r") as file_in, open(destination_file_name, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
