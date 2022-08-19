import shutil


def copy_file(command: str):
    list_command = command.split()
    source = list_command[1]
    destination = list_command[2]
    if source != destination:
        shutil.copyfile(source, destination)
