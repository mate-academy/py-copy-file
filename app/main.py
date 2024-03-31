def copy_file(command: str) -> None:
    command_list = command.split()

    if command_list[0] != "cp":
        return

    source_file, destination_file = command_list[1], command_list[2]

    if source_file == destination_file:
        return

    with open(source_file, "r") as file_in, open(destination_file, "w") as file_out:
        file_out.write(file_in.read())
