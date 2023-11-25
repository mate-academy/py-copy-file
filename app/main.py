def copy_file(command: str):
    command_list = command.split()

    source_file, destination_file = command_list[1], command_list[2]

    if source_file != destination_file:
        with open(source_file, "r") as file_in, open(destination_file, "w") as file_out:
            file_out.write(file_in.read())
