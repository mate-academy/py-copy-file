def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "cp":
        return None
    file_name = command[1]
    file_copy_name = command[2]
    if file_name == file_copy_name:
        return None
    try:
        with (open(file_name, "r") as file_read,
              open(file_copy_name, "w") as file_copy):
            file_copy.write(file_read.read())
    except FileNotFoundError:
        return None
