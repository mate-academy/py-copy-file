def copy_file(command: str) -> None | str:
    command_parts = command.split()
    try:
        if (
                len(command_parts) == 3
                and command_parts[0] == "cp"
                and command_parts[1] != command_parts[2]
        ):
            with (
                open(command_parts[1], "r") as source_file,
                open(command_parts[2], "w") as destination_file
            ):
                destination_file.write(source_file.read())
    except FileNotFoundError:
        return f"File {command_parts[1]} does not exist"
