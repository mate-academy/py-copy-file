import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source, destination = parts

    if source == destination:
        return

    if not os.path.exists(source):
        print(f"Error: Source file '{source}' does not exist.")
        return

    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
