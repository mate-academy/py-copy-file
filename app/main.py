def copy_file(command: str) -> None:
    parsed_command = command.split(" ")
    if len(parsed_command) != 3 or parsed_command[0] != "cp":
        return
    com, source, destination = parsed_command
    if source == destination:
        return
    try:
        with (
            open(source) as old_file,
            open(destination, "w") as new_file
        ):
            for line in old_file:
                new_file.write(line)
    except FileNotFoundError:
        return
