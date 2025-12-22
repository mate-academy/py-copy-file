def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, src, dest = parts

    if src == dest:
        return

    try:
        with open(src, "r") as file_in:
            content = file_in.read()

        with open(dest, "w") as file_out:
            file_out.write(content)

    except FileNotFoundError:
        return
