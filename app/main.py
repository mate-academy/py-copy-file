def copy_file(command: str) -> None:
    command_parts = command.split()
    command, source_file, destination_file = command_parts

    if (
            source_file != destination_file
            and len(command_parts) == 3
            and command == "cp"):
        with open(
                source_file,
                "r"
        ) as file_in, open(
            destination_file,
            "w"
        ) as file_out:
            file_out.write(file_in.read())
