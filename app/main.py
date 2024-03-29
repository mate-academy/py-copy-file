def copy_file(command: str) -> None:
    commands = command.split()
    if len(commands) != 3 or commands[0] != "cp" or commands[1] == commands[2]:
        return

    _, copied_file, new_file = commands
    with open(copied_file, "r") as c_file, open(new_file, "w") as n_file:
        n_file.write(c_file.read())
