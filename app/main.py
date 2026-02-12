
def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        return None
    if command_parts[0] != "cp":
        return None
    source_file_name = command_parts[1]
    dest_file_name = command_parts[2]
    if source_file_name == dest_file_name:
        return None
    try:
        with (open(source_file_name, "r") as file_in,
                open(dest_file_name, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return None
