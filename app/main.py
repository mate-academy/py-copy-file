import shutil
import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command format. "
              "Please use 'cp source_file destination_file'.")
        return

    source_file = parts[1]
    destination_file = parts[2]

    if source_file == destination_file:
        print("Source file and destination file have the same name. "
              "No action taken.")
        return

    if os.path.exists(destination_file):
        print("Destination file already exists. No action taken.")
        return

    try:
        shutil.copyfile(source_file, destination_file)
        print(f"File '{source_file}' copied to "
              f"'{destination_file}' successfully.")
    except FileNotFoundError:
        print("Source file does not exist.")
    except PermissionError:
        print("Permission denied. Cannot copy the file.")
    except Exception as e:
        print(f"An error occurred: {e}")
