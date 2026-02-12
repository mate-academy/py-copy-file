def copy_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    first_file = parts[1]
    second_file = parts[2]

    try:
        with open(first_file, "rb") as ff, open(second_file, "wb") as sf:
            sf.write(ff.read())
    except FileNotFoundError:
        return
