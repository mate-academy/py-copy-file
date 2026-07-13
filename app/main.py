from pathlib import Path


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    if parts[2] == parts[1]:
        return
    if not Path(parts[1]).is_file():
        return
    with open(parts[1], "r") as file_out, open(parts[2], "w") as file_in:
        for line in file_out:
            file_in.write(line)
