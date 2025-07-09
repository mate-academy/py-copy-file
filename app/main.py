def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    _, src, dst = parts

    if src == dst:
        return

    try:
        with (open(src, "r") as file_in,
              open(dst, "w") as file_out):
            for line in file_in:
                file_out.write(line)
    except FileNotFoundError:
        pass
