def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    src = parts[1]
    dst = parts[2]
    if src == dst:
        return
    try:
        with open(src, "r") as file_in:
            content = file_in.read()
    except FileNotFoundError:
        return

    with open(dst, "w") as file_out:
        file_out.write(content)
