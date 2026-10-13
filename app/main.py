import os
import shlex


def copy_file(command: str) -> None:
    if not command:
        return

    try:
        parts = shlex.split(command)
    except ValueError:
        return

    if len(parts) != 3:
        return

    source, target = parts[1], parts[2]

    if source == target:
        return

    if not os.path.exists(source):
        return

    try:
        with open(source, "r", encoding="utf-8") as src_file, \
            open(target, "w", encoding="utf-8") as dst_file:
            dst_file.write(src_file.read())
    except OSError:
        return
