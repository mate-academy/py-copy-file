def copy_file(command: str) -> None:
    command_parts = command.split()

    if len(command_parts) != 3:
        print("Error: Command format is incorrect.")
        return

    cmd, source_file, destination_file = command_parts

    if cmd != "cp" or source_file == destination_file:
        return
    with open(source_file, "r") as source, open(destination_file, "w") as copy:
            copy.write(source.read())
