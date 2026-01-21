import os


def copy_file(line: str) -> None:
    command_parts = line.split()
    text = ""
    if len(command_parts) < 3 or command_parts[0] != "cp":
        return

    if command_parts[1] == command_parts[2]:
        return

    if not os.path.exists(command_parts[1]):
        return

    with open(command_parts[1], "r") as f:
        text = f.read()

    with open(command_parts[2], "w") as f:
        f.write(text)
