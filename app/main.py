import os


def copy_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source, target = parts

    if source == target:
        return

    if not os.path.exists(source):
        return

    with open(source, "r", encoding="utf-8") as file_in, open(
        target, "w", encoding="utf-8"
    ) as file_out:
        file_out.write(file_in.read())
