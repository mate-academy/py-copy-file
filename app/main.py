def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) < 3 or command_parts[0] != "cp":
        return
    orig_file = command_parts[1]
    new_file = command_parts[2]
    if orig_file == new_file:
        return
    try:
        with (open(orig_file, "r") as file_in,
              open(new_file, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return
