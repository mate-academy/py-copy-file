def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) == 3 or parts[0] != "cp":
        return
    source_file = command.split()[1]
    target_file = command.split()[2]
    if ".txt" not in source_file or ".txt" not in target_file:
        return
    if source_file == target_file:
        return
    try:
        with open(source_file, "r") as source,open(target_file, "w")as target:
            target.write(source.read())
    except FileNotFoundError:
        ...
