import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file = parts[1]
    target_file = parts[2]

    if source_file == target_file:
        return

    if not os.path.exists(source_file):
        return

    with (
        open(source_file, "r") as file_in,
        open(target_file, "w") as file_out
    ):
        content = file_in.read()
        file_out.write(content)
