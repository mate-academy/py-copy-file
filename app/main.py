def copy_file(command: str) -> None:
    command_details = command.split()
    if (
            len(command_details) < 3
            or command_details[1] == command_details[2]
            or command_details[0] != "cp"
    ):
        return

    source_file_name = command_details[1]
    new_file_name = command_details[2]

    try:
        with (
            open(source_file_name, "r") as source_f,
            open(new_file_name, "w") as new_f
        ):
            new_f.write(source_f.read())
    except FileNotFoundError:
        return
