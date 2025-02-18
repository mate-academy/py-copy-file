def copy_file(command: str) -> None:
    command = command.split()

    if len(command) != 3 or command[0] != "cp":
        raise Exception("Invalid command")

    _, file_name, copy_name = command

    if file_name != copy_name:
        with open(file_name, "r") as file, open(copy_name, "w") as copy:
            copy.write(file.read())
