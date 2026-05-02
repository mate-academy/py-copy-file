def copy_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, src_file, dst_file = parts

    if src_file == dst_file:
        return

    try:
        with open(src_file, "rb") as file_in, open(dst_file, "wb") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
