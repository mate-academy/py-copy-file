def copy_file(command: str) -> None:
    commands = command.split(" ")

    source_file, destination_file = commands[1], commands[2]

    if source_file == destination_file:
        return

    file_in = open(source_file, "r")
    file_out = open(destination_file, "w")
    file_out.write(file_in.read())
