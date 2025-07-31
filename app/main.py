def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    src = parts[1]
    dst = parts[2]
    if src == dst:
        return
    try:
        file_in = open(src, "r")
    except FileNotFoundError:
        return
    content = file_in.read()
    file_in.close()

    file_out = open(dst, "w")
    file_out.write(content)
    file_out.close()
