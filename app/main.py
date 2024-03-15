def copy_file(command: str) -> None:
    command = command.split()
    if len(command) != 3 or command[0] != "cp":
        raise ValueError("Use: cp <file> <file_copy>")
    file_name, copy_name = command[1:]
    if command[file_name] != command[copy_name]:
        with (
            open(command[file_name], "r") as file_to_copy,
            open(command[copy_name], "w") as file_to_paste
        ):
            file_to_paste.write(file_to_copy.read())
