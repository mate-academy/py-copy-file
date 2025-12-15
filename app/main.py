import os


def copy_file(command: str) -> None:
    part_command = command.split()

    if len(part_command) != 3 or part_command[0] != "cp":
        return

    old_file, new_file = part_command[1], part_command[2]

    if old_file == new_file:
        return

    if not os.path.exists(old_file):
        if os.path.exists(new_file):
            os.remove(new_file)
        return

    with open(old_file, "r") as source, open(new_file, "w") as target:
        target.write(source.read())
