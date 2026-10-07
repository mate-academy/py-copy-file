def copy_file(command: str) -> None:
    parts_of_command = command.split(" ")
    if len(parts_of_command) != 3 or parts_of_command[0] != "cp":
        return
    _, name_in, name_out = parts_of_command
    if name_in == name_out:
        return
    try:
        with open(name_in, "r") as file_in, open(name_out, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
