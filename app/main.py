import shutil
import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        print("Invalid command format. "
              "Please provide command in the format: "
              "cp source_file target_file")
        return

    source_file, target_file = parts[1], parts[2]

    if source_file == target_file:
        print("Source file and target file are the same. No action taken.")
        return

    if os.path.exists(target_file):
        print("Target file already exists. No action taken.")
        return

    shutil.copyfile(source_file, target_file)
    print(f"File '{source_file}' copied to '{target_file}' successfully.")
