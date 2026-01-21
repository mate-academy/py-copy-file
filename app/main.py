import os


def copy_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file_name, target_file_name = parts[1], parts[2]

    if source_file_name == target_file_name:
        return

    if not os.path.isfile(source_file_name):
        return

    with open(source_file_name, "r", encoding="utf-8") as source_file, \
         open(target_file_name, "w", encoding="utf-8") as target_file:
        target_file.write(source_file.read())
