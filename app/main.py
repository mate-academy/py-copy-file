def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    src_file = parts[1]
    dst_file = parts[2]

    if src_file == dst_file:
        return

    try:
        with open(src_file, "r") as f_in, open(dst_file, "w") as f_out:
            f_out.write(f_in.read())
    except FileNotFoundError:

        pass
