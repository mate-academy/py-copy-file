def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    command_name, file_in_name, file_out_name = parts
    if command_name != "cp":
        return
    if file_in_name == file_out_name or not file_in_name:
        return
    try:
        with (open(file_in_name, "r") as file_in,
              open(file_out_name, "w") as file_out):
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        return
