import os


def copy_file(command: str) -> None:
    parts = command.split(" ")

    if parts[0] != "cp":
        return
    if len(parts) != 3:
        return
    if parts[1] == parts[2]:
        return
    if not os.path.exists(parts[1]):
        return

    with open(parts[1], "r") as file_in, open(parts[2], "w") as file_out:
        text = file_in.read()
        file_out.write(text)
