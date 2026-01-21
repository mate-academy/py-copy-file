import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        print("Invalid command")
        return

    source_file, destination_file = parts[1], parts[2]
    if source_file == destination_file:
        print("Source file cannot be equal to destination file")
        return

    if not os.path.exists(source_file):
        print("Source file does not exist")
        return

    try:
        with open(source_file, "rb") as f1, open(destination_file, "wb") as f2:
            f2.write(f1.read())
    except FileNotFoundError:
        print(f"Error: The file '{source_file}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing "
              f"'{source_file}' or '{destination_file}'.")
    except OSError as e:
        print(f"Error: {e}")
