def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    _, src_name, dst_name = parts

    if parts[0] != "cp":
        return

    if src_name == dst_name:
        return

    try:
        with open(src_name, "r") as file_in, open(dst_name, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
