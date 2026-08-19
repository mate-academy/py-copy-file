import os


def copy_file(command: str) -> None:
    parts: list[str] = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source: str = parts[1]
    destination: str = parts[2]

    if source == destination or not os.path.isfile(source):
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
