def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    source = command.split()[1]
    target = command.split()[2]
    if ".txt" not in source or ".txt" not in target:
        return
    if source == target:
        return
    try:
        with open(source, "r") as source, open(target, "w") as target:
            target.write(source.read())
    except FileNotFoundError:
        ...
