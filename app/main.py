def copy_file(command: str) -> None:
    split_command = command.split()
    source_file = split_command[1]
    new_file = split_command[2]
    if source_file != new_file:
        with open(source_file, "r") as source, open(new_file, "w") as file_out:
            file_out.write(source.read())
