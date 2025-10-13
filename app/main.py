import os


def copy_file(command: str) -> None:
    parts = command.strip().split()

    # Validate command format
    if len(parts) != 3 or parts[0] != "cp":
        return

    source, target = parts[1], parts[2]

    # Do nothing if source and target are the same
    if source == target:
        return

    # Check if source file exists
    if not os.path.exists(source):
        return

    # Copy content
    with open(source, "r") as file_in, open(target, "w") as file_out:
        file_out.write(file_in.read())
