def copy_file(command: str) -> None:
    command = command.split(" ")

    if command[1] == command[2]:
        pass

    with open(command[1], "r") as data_file:
        data = data_file.read()
        with open(command[2], "w") as new_file:
            new_file.write(data)
