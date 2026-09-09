from pathlib import Path


def copy_file(command: str) -> None:
    split_command = command.split(" ")
    if len(split_command) != 3 or split_command[0] != "cp":
        return None
    file_path = Path(split_command[1])
    source_file = split_command[1]
    copy_file = split_command[2]
    if source_file == copy_file or not file_path.is_file():
        return None
    with open(
        source_file, "r", encoding="utf-8"
    ) as file, open(copy_file, "w", encoding="utf-8") as file_out:
        file_out.write(file.read())
