def copy_file(command: str) -> None:

    split_command = command.split()
    if not command or split_command[0] != "cp":
        return

    try:
        source_file_name = split_command[1]
        destination_file_name = split_command[2]
    except IndexError:
        return

    if source_file_name == destination_file_name:
        return
    try:
        with (
            open(source_file_name, "r") as source_file,
            open(destination_file_name, "w") as destination_file
        ):
            for line in source_file:
                destination_file.write(line)
    except FileNotFoundError:
        return
