def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file = parts[1]
    new_file = parts[2]

    if source_file == new_file:
        return

    try:
        with open(source_file, "r") as f, open(new_file, "w") as f_out:
            f_out.write(f.read())
    except FileNotFoundError:
        return
