def copy_file(command: str) -> None:
    # 1. Split the command to get source and destination
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    source = parts[1]
    dest = parts[2]

    # 2. Check if they're the same
    if source == dest:
        return

    # 3. Copy the content
    try:
        with open(source, "r") as source_file, open(dest, "w") as target_file:
            target_file.write(source_file.read())
    except FileNotFoundError:
        return
