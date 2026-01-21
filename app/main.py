def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    command_name, source_file_name, destination_file_name = parts
    if command_name != "cp":
        return
    if source_file_name == destination_file_name:
        return
    try:
        with (open(source_file_name, "r", encoding="utf-8") as file_in,
              open(destination_file_name, "w", encoding="utf-8") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
