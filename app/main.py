def copy_file(command: str) -> None:
    if not isinstance(command, str):
        return
    command_parts = command.split()
    if len(command_parts) != 3:
        return
    command_name, source_file, destination_file = command_parts
    if command_name != "cp":
        return
    if source_file == destination_file:
        return
    try:
        with open(source_file, "r") as file_name_in, \
                open(destination_file, "w") as file_name_out:
            text = file_name_in.read()
            file_name_out.write(text)
    except FileNotFoundError:
        return
