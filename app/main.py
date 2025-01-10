import shutil
import os


def copy_file(command: str) -> None:
    parts = command.split()

    if parts[0] != "cp" or len(parts) != 3:
        raise ValueError(
            "Invalid format. "
            "Expected: 'cp file.txt file-copy.txt'"
        )

    source_file = parts[1]
    destination_file = parts[2]

    if source_file == destination_file:
        return

    if not os.path.exists(source_file):
        print(f"Error: '{source_file}' not found!")
        return

    try:
        shutil.copy(source_file, destination_file)
        print(f"File '{source_file}' copied to '{destination_file}'")
    except Exception as e:
        print(f"Error: {e}")
