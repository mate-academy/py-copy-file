def copy_file(command: str) -> None:
    parts = command.split()
    if not (len(parts) == 3 and parts[0] == "cp"):
        return

    src, dst = parts[1], parts[2]

    if src == dst:
        return

    try:
        with open(src, "rb") as f_in, open(dst, "wb") as f_out:
            f_out.write(f_in.read())
    except FileNotFoundError:
        print(f"Error: file '{src}' not found.")
