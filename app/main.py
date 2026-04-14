
def copy_file(command: str) -> None:
    parts = command.split(maxsplit=2)
    if len(parts) != 3 or parts[0] != "cp":
        return
    src, dst = parts[1], parts[2]
    if src == dst:
        return
    try:
        with open(src, "rb") as f_in, open(dst, "wb") as f_out:
            for line in f_in:
                f_out.write(line)
    except FileNotFoundError:
        return
