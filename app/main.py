def copy_file(command: str) -> None:
    if not command:
        return
    command_parts = command.split()
    if command_parts[0] != "cp" or len(command_parts) != 3:
        return
    source_file = command_parts[1]
    destination_file = command_parts[2]
    if source_file == destination_file:
        return
    try:
        with (open(source_file , "r") as file_in,
              open(destination_file, "w") as file_out):
            data = file_in.read()
            file_out.write(data)
    except FileNotFoundError:
        return
