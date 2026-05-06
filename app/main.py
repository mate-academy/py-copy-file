def copy_file(command: str) -> None:
    split_command = command.split(" ")
    if command and len(split_command) == 3 and split_command[0] == "cp":
        cp, file_name, new_file_name = split_command
        if file_name != new_file_name:
            try:
                with (open(file_name, "r") as file_in,
                      open(new_file_name, "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError as e:
                return e
    return None
