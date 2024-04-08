import shutil


def copy_file(command: str) -> None:
    if command.startswith("cp "):
        _, source_file, destination_file = command.split()
        if source_file != destination_file:
            try:
                shutil.copy(source_file, destination_file)
            except FileNotFoundError:
                print("Source file not found.")
            except IOError as e:
                print(f"Error copying file: {e}")
