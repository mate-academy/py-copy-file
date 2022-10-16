def copy_file(command: str) -> None:
    command = command.split(" ")
    with open(command[1], "r") as file_from, open(command[2], "a") as file_to:
        for line in file_from.readlines():
            file_to.write(line)
