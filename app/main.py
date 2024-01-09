import shutil


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "cp":
        source_path, destination_path = parts[1:]
        if source_path != destination_path:
            shutil.copyfile(source_path, destination_path)
    else:
        print("Invalid command. Usage: cp <source_file> <destination_file>")
