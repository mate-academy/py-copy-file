from os import path
from logging import debug
import os


def copy_file(command: str) -> None:
    print(command)
    operators = command.split(" ")
    if len(operators) != 3:
        return

    cmd, cp_name, file_name = operators

    if cmd != "cp":
        print(cmd)
        return

    if not path.exists(cp_name):
        print(cp_name)
        return

    current_path = os.getcwd()
    copy_path = os.path.join(current_path, file_name)

    if cp_name != file_name:
        try:
            with open(cp_name, "r") as first:
                with open(copy_path, "w") as second:
                    second.write(first.read())
        except Exception as e:
            debug(e)

    print(copy_file)
