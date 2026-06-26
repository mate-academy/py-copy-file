def copy_file(command: str) -> None:
    if (not len(command)
            or command.split()[0] != "cp"
            or len(command.split()) != 3
            or command.split()[1] == command.split()[2]):
        return
    try:
        with open(command.split()[1], "r") as old_file:
            new_file = open(command.split()[2], "w")
            new_file.write(old_file.read())
            new_file.close()
        old_file.close()
    except FileNotFoundError:
        pass
