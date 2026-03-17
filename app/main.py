def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    if parts[0] != "cp":
        return

    source, target = parts[1], parts[2]
    if source == target:
        return

    try:
        with open(source, "r", encoding="utf-8") as file_in, open(
            target, "w", encoding="utf-8"
        ) as file_out:
            file_out.write(file_in.read())
    except OSError:
        return
