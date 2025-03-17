import shutil
import os


def copy_file(command: str) -> str:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format. Use: cp <source> <destination>")
        return

    source, destination = parts[1], parts[2]

    if not os.path.isfile(source):
        print(f"Error: Source file '{source}' does not exist.")
        return

    if source == destination:
        print("Error: Source and destination file names are"
              " the same. No action taken.")
        return

    try:
        shutil.copy(source, destination)
        print(f"File '{source}' copied to '{destination}' successfully.")
    except Exception as e:
        print(f"Error copying file: {e}")


copy_file("cp file.txt file-copy.txt")
