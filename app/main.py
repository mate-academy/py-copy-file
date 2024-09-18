import shutil


def copy_file(command: str) -> None:
    file, new_file = command.split()[1], command.split()[2]
    if file != new_file:
        shutil.copy(file, new_file)
