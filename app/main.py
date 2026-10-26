def copy_file(command: str) -> None:
    command_parts = command.split(" ")
    if len(command_parts) != 3 or command_parts[0] != "cp":
        return
    c_file = command_parts[1]
    new_file = command_parts[2]
    if c_file == new_file:
        return
    try:
        with open(c_file, "r") as file_in, open(new_file, "w") as file_out:
            file_content = file_in.read()
            file_out.write(file_content)
    except FileNotFoundError:
        return
