def copy_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3:
        raise ValueError("The command must be 'cp file.txt new_file.txt'")
    if split_command[0] != "cp":
        raise ValueError("The command should be 'cp'")
    source_file = split_command[1]
    new_file = split_command[2]
    if source_file != new_file:
        with open(source_file, "r") as source, open(new_file, "w") as file_out:
            file_out.write(source.read())
