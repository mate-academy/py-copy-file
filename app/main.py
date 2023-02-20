def copy_file(command: str) -> None:
    commands = command.split()
    if commands[0] == "cp" and commands[1] != commands[2]:
        with (
            open(commands[1], "r") as file_in,
            open(commands[2], "w") as file_out
        ):
            file_out.write(file_in.read())
