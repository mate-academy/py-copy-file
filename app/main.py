import os
import shutil


def copy_file(command: str) -> None:
    commands = command.split()
    if (
            len(commands) != 3
            or commands[0] != "cp"
            or commands[1] == commands[2]
    ):
        print(f"Please check you command {command}. Something went wrong.")
        return
    if not os.path.exists(commands[1]):
        print(f"The file {commands[1]} does not exist.")
        return
    shutil.copy(commands[1], commands[2])
