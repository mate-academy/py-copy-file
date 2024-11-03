import shutil


def copy_file(command: str) -> None:
    commands = command.split(" ")
    if len(commands) != 3 or not commands[0] == "cp" or commands[1] == commands[2]:
        return
    shutil.copy(commands[1], commands[2])
