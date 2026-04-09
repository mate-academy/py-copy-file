def copy_file(command: str) -> None:
    parts = command.split()
    src = parts[1]
    dst = parts[2]

    if src == dst:
        return

    with open(src, "r") as file_in, open(dst, "w") as file_out:
        file_out.write(file_in.read())
