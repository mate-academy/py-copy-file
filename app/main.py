def copy_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3 or split_command[0] != "cp":
        return

    current_file = split_command[1]
    new_file = split_command[2]

    if current_file == new_file:
        return

    with open(current_file, "r") as file_in, open(new_file, "w") as file_out:
        file_out.write(file_in.read())
