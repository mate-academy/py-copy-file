def copy_file(command: str) -> None:
    command = command.split()
    with open(command[1], "r") as file_in, open(command[2], "w") as file_out:
        if file_in == file_out:
            return
        file_out.write(file_in.read())
