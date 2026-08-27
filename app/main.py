def copy_file(command: str) -> None:
    parsed_command = command.split()
    if (
            len(parsed_command) != 3
            or parsed_command[0] != "cp"
            or parsed_command[1] == parsed_command[2]
    ):
        return
    _, source, destination = parsed_command
    try:
        with (
            open(source) as old_file,
            open(destination, "w") as new_file
        ):
            for line in old_file:
                new_file.write(line)
    except FileNotFoundError:
        return
