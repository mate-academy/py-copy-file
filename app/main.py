def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file = parts[1]
    target_file = parts[2]
    if source_file == target_file:
        return
    try:
        with (open(source_file, "r") as f1,
              open(target_file, "w") as f2):
            f2.write(f1.read())
    except FileNotFoundError:
        return
