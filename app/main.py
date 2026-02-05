import shutil


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 and parts[0] == "cp":
        _, source_file_name, copied_file_name = parts
        if source_file_name == copied_file_name:
            return
        try:
            shutil.copy(source_file_name, copied_file_name)
        except FileNotFoundError:
            return
