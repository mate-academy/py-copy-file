import os


def copy_file(command: str) -> None:
    command_parts = command.strip().split()

    if (
        len(command_parts) != 3
        or command_parts[0] != "cp"
    ):
        return

    source_file_path = command_parts[1]
    destination_file_path = command_parts[2]

    if not source_file_path or not destination_file_path:
        return

    if (
        os.path.isdir(source_file_path)
        or os.path.isdir(destination_file_path)
    ):
        return

    if (
        not os.path.isfile(source_file_path)
        or source_file_path == destination_file_path
    ):
        return

    destination_dir = os.path.dirname(destination_file_path)
    if destination_dir:
        os.makedirs(destination_dir, exist_ok=True)

    try:
        with open(source_file_path, "r") as source_file:
            with open(destination_file_path, "w") as destination_file:
                destination_file.writelines(source_file)
    except (FileNotFoundError, PermissionError, OSError):
        return
