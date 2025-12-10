def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return command

    source_file = parts[1]
    target_file = parts[2]

    if source_file == target_file:
        return

    try:
        with open(source_file, "r") as source:
            content = source.read()
    except FileNotFoundError:
        return

    with open(target_file, "w") as target:
        target.write(content)
