def copy_file(command: str) -> None:
    arguments = [word for word in command.split()]
    if arguments[1] == arguments[2]:
        return
    with open(arguments[1], "r") as file, open(arguments[2], "w") as new_file:
        new_file.write(file.read())
