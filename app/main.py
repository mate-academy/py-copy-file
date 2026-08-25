from os import path


def copy_file(command: str) -> None:
    commands = command.split(" ")
    if len(commands) == 3 and commands[0] == "cp":
        if commands[1] != commands[2]:
            if path.exists(commands[1]):
                with (open(commands[1], "r") as file_in,
                      open(commands[2], "w") as file_out):
                    file_out.write(file_in.read())
