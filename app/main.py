import shutil


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    original_file, new_file = parts[1:]

    if original_file != new_file:
        with (
            open(original_file, "r") as file_in,
            open(new_file, "w") as file_out
        ):
            shutil.copyfileobj(file_in, file_out)
