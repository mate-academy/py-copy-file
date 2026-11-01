def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) == 3 and command_parts[0] == "cp":
        source_name = command_parts[1]
        destination_name = command_parts[2]
        if source_name == destination_name:
            return
        try:
            with open(source_name, "r") as source_file, open(
                destination_name, "w"
            ) as destination_file:
                destination_file.write(source_file.read())
        except FileNotFoundError:
            return