def copy_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    scr = parts[1]
    dst = parts[2]
    if scr == dst:
        return
    try:
        with (open(scr, "r") as file_in,
              open(dst, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
