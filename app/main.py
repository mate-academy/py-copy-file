import os


def copy_file(command: str) -> None:
    if not command:
        return

    parts = command.split(" ")

    if parts[0] != "cp" or len(parts) != 3:
        return

    source = parts[1]
    destination = parts[2]

    if source == destination:
        return

    if not os.path.exists(source):
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        content = file_in.read()
        file_out.write(content)
