import shutil


def copy_file(command: str):
    new_command = command.split()
    file = new_command[1]
    new_file = new_command[2]

    if file != new_file:
        shutil.copy(file, new_file)
