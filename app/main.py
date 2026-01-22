def copy_file(command: str) -> None:
    command = command.split(" ")

    if command[0] != "cp":
        raise NameError("Cannot recognize the command")

    with open(command[1], "r") as file_from, open(command[2], "a") as file_to:
        for line in file_from.readlines():
            file_to.write(line)
