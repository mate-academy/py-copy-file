def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        command_name, source_file_name, destination_file_name = command.split()

        if (
            source_file_name != destination_file_name
            and command_name == "cp"
        ):
            with (
                open(source_file_name, "r") as source,
                open(destination_file_name, "w") as destination
            ):
                destination.write(source.read())
