def copy_file(command: str) -> None:
    command_parts = command.split()
    if len(command_parts) != 3:
        return
    file1 = command_parts[1]
    file2 = command_parts[2]
    if file1 == file2:
        return
    if command_parts[0] == "cp":
        try:
            with open(file1, "r") as file_in, open(file2, "w") as file_out:
                file_out.write(file_in.read())
        except FileNotFoundError:
            return
    else:
        return
