from __future__ import annotations

import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    cmd, source, target = parts
    if cmd != "cp":
        return
    if source == target:
        return
    if not os.path.isfile(source):
        return

    with open(source, "rb") as file_in, open(target, "wb") as file_out:
        file_out.write(file_in.read())
