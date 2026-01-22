def copy_file(comm: str) -> None:
    parts = comm.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    src, dst = parts[1], parts[2]

    if src == dst:
        return

    try:
        with open(src, "rb") as file_in, open(dst, "wb") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
