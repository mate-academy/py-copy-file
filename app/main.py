from typing import List


def copy_file(command: str) -> None:
    parts: List[str] = command.split()

    if len(parts) != 3:
        return

    _, source_file, target_file = parts

    if source_file == target_file:
        return

    with open(source_file, "r") as file_in, open(target_file, "w") as file_out:
        file_out.write(file_in.read())
