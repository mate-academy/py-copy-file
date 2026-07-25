def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    command_name, file_to_read, file_to_write = parts

    if file_to_read == file_to_write or command_name != "cp":
        return

    try:
        with (open(file_to_read, "r") as file_in,
              open(file_to_write, "w") as file_out):
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        return
