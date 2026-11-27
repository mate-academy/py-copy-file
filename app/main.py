import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source_file_name, target_file_name = parts

    if (
        source_file_name == target_file_name
        or not os.path.exists(source_file_name)
    ):
        return

    with (
        open(source_file_name, "r", encoding="utf-8") as file_in,
        open(target_file_name, "w", encoding="utf-8") as file_out,
    ):
        file_out.write(file_in.read())
