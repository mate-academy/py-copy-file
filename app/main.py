import os


def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] not in ("cp", "copy"):
        return

    file_name, copy_name = parts[1], parts[2]

    if file_name == copy_name:
        return

    if not os.path.exists(file_name):
        return

    try:
        with open(file_name, "rb") as src, open(copy_name, "wb") as dst:
            for chunk in iter(lambda: src.read(4096), b""):
                dst.write(chunk)
    except Exception:
        return
