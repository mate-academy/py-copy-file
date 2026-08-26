import shutil


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) < 3 or parts[0] != "cp":
        return

    _, src_file, dest_file = parts

    if src_file == dest_file:
        return

    try:
        shutil.copyfile(src_file, dest_file)
    except FileNotFoundError:
        return
