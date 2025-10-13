def copy_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) < 3 or split_command[0] != "cp":
        return
    file_to_copy = split_command[1]
    new_file_name = split_command[2]
    try:
        if file_to_copy != new_file_name:
            with (
                open(file_to_copy, "r") as file_in,
                open(new_file_name, "w") as file_out
            ):
                file_out.write(file_in.read())
    except FileNotFoundError:
        return
