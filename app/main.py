def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    src = parts[1]
    dst = parts[2]
    if src == dst:
        return
    try:
        with open(src, "r") as f_in, open(dst, "w") as f_out:
            f_out.write(f_in.read())
    except FileNotFoundError:
        return
