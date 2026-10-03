def copy_file(command: str) -> bool:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return False
    source, dest = parts[1], parts[2]
    if source == dest:
        return True
    try:
        with open(source, "r") as src_in, open(dest, "w") as dst_out:
            content = src_in.read()
            dst_out.write(content)
            return True
    except FileNotFoundError:
        return False
