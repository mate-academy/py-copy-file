import os


def copy_file(command: str) -> None:
    command_parts: list[str] = command.split()

    if len(command_parts) != 3:
        return

    if command_parts[0] != "cp":
        return

    source_filename: str = command_parts[1]
    target_filename: str = command_parts[2]

    if source_filename == target_filename:
        return

    if not os.path.exists(source_filename):
        return

    with open(source_filename, "r") as source_file, \
         open(target_filename, "w") as target_file:
        file_content: str = source_file.read()
        target_file.write(file_content)
