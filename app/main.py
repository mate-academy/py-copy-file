def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    src = parts[1]
    dest = parts[2]
    if src == dest:
        return
    try:
        with open(src, "r") as file_in, open(dest, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return
