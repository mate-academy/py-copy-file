def copy_file(command: str) -> None:
    parts = command.strip().split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, src_file, dest_file = parts

    if src_file == dest_file:
        return

    try:
        with open(src_file, "r") as file_in, open(dest_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
