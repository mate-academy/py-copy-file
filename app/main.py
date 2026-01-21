import os


def copy_file(input_command: str) -> None:
    parts = input_command.split(" ")
    if len(parts) != 3:
        print("Invalid command format. Correct format: cp source target")
        return

    command, source, target = parts
    if command != "cp":
        print(f"Unsupported command: {command}")
        return

    if source == target:
        print("Source and target files are the same. Nothing to do.")
        return

    if not os.path.exists(source):
        print(f"Source file '{source}' does not exist.")
        return

    try:
        with open(source, "rb") as file_in, open(target, "wb") as file_out:
            file_out.write(file_in.read())
        print(f"File copied successfully from '{source}' to '{target}'.")
    except Exception as e:
        print(f"Error copying file: {e}")
