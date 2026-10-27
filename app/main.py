def copy_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3 or command_list[0] != "cp":
        return

    source_file = command_list[1]
    destination_file = command_list[2]

    if source_file == destination_file:
        return

    try:
        with open(source_file, "r") as file_in:
            file_output = file_in.read()
    except FileNotFoundError:
        return

    with open(destination_file, "w") as file_out:
        file_out.write(file_output)
