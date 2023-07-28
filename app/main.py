def copy_file(command: str) -> None:
    split_command = command.split(" ")
    command = split_command[0]
    file_out = split_command[1]
    file_in = split_command[2]

    if command == "cp" and file_out != file_in:
        with open(file_out, "r") as file_from, open(file_in, "w") as file_to:
            file_to.write(file_from.read())
