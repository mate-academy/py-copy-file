def copy_file(command: str) -> None:
    command_parts = command.split()

    if command_parts[0] != "cp":
        raise ValueError("The command need to start with 'cp'")

    if len(command_parts) != 3:
        raise ValueError("Command format needs to be <cp file_1 file_2>")

    if command_parts[1] != command_parts[2]:
        with (open(command_parts[1], "r") as source_file,
              open(command_parts[2], "w") as destination_file):
            destination_file.write(source_file.read())
