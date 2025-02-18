def copy_file(command: str) -> None:
    commands = command.split(" ")
    if commands[1] == commands[2] or len(commands) != 3 or commands[0] != "cp":
        return
    with open(commands[1], "r") as file_in, open(commands[2], "w") as file_out:
        file_out.write(file_in.read())
