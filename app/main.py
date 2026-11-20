def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return None

    command_name = parts[0]
    file_name = parts[1]
    new_file_name = parts[2]

    if command_name != "cp":
        return None

    if file_name == new_file_name:
        return None

    try:
        with (open(file_name, "r") as file_in,
              open(new_file_name, "w") as file_out):
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return None
