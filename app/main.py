import os


def copy_file(command: str) -> None:
    if not len(command):
        return

    splited_command = command.split()

    if len(splited_command) != 3:
        return

    [action, source, target] = splited_command

    if action != "cp":
        return

    if source == target:
        return

    if not os.path.exists(source):
        return

    with open(source, "r") as source_file, open(target, "w") as target_file:
        target_file.write(source_file.read())
