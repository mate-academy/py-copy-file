import os


def copy_file(command: str) -> None:

    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    _, original_file, new_file = parts
    if original_file == new_file:
        return

    if not os.path.exists(original_file):
        return

    with (open(original_file, "r") as file_in,
          open(new_file, "w") as file_out):
        content = file_in.read()
        file_out.write(content)
