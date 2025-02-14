def copy_file(command: str) -> None:
    split_command = command.split()
    if split_command[1] != split_command[2]:
        or_file, cp_file = split_command[1], split_command[2]
        with open(or_file, "r") as file_in, open(cp_file, "w") as file_out:
            file_out.write(file_in.read())
