import os
import shutil


def copy_file(command: str) -> None:
    if not command:
        return
    command = command.split()
    if len(command) != 3 or command[0] != "cp":
        return
    file_from = command[1]
    file_copy = command[2]
    if file_from == file_copy:
        return
    if not os.path.exists(file_from):
        return
    shutil.copy(file_from, file_copy)
