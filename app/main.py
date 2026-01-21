import shutil
import os


def copy_file(command: str):
    # Split the command into parts
    parts = command.split()

    # Validate the command format
    if len(parts) != 3 or parts[0] != "cp":
        raise ValueError("Invalid command format. Use: cp <source> <destination>")

    source, destination = parts[1], parts[2]

    # Check if source and destination are the same
    if source == destination:
        return  # Do nothing

    # Check if source file exists
    if not os.path.exists(source):
        raise FileNotFoundError(f"Source file '{source}' does not exist.")

    # Perform the copy operation
    with open(source, "r") as file_in, open(destination, "w") as file_out:
        file_out.write(file_in.read())
