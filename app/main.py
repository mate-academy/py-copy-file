def copy_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    _, src, dst = parts

    if src == dst:
        return

    try:
        with open(src, "r") as file_in, open(dst, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        print(f"Error: source file '{src}' does not exist.")
