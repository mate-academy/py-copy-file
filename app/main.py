def copy_file(command: str) -> None:
    command_name = command.split()[0]
    source_file_name = command.split()[1]
    destination_file_name = command.split()[2]

    if (source_file_name != destination_file_name) and (command_name == "cp"):
        with (
            open(source_file_name, "r") as source,
            open(destination_file_name, "w") as destination
        ):
            destination.write(source.read())
