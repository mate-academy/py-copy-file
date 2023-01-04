import shutil


def copy_file(command: str) -> None:
    if command.split()[1] != command.split()[2]:
        shutil.copy(f"{command.split()[1]}", f"{command.split()[2]}")
