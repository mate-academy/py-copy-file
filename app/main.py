import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    action, source, target = parts
    if action != "cp":
        return
    if source == target:
        return
    if not os.path.exists(source):
        return

    with open(source, "r") as file_in, open(target, "w") as file_out:
        file_out.write(file_in.read())
