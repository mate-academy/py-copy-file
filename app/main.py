def copy_file(command: str) -> None:
    try:
        command_name, source_file_name, destination_file_name = command.split()
    except ValueError:
        return
    if command_name != "cp":
        return
    try:
        if source_file_name != destination_file_name:
            with (open(source_file_name, "r") as file_in,
                  open(destination_file_name, "w") as file_out):
                content = file_in.read()
                file_out.write(content)
    except FileNotFoundError:
        return
    return
