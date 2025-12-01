import os


def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return None
    if parts[0] != "cp":
        return None
    src = parts[1]
    dst = parts[2]
    if src == dst:
        return None
    if not os.path.isfile(src):
        return None
    with open(src, "rb") as fsrc, open(dst, "wb") as fdst:
        chunk = fsrc.read(4096)
        while chunk:
            fdst.write(chunk)
            chunk = fsrc.read(4096)
