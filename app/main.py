def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    _, source_name, target_name = parts
    if source_name == target_name:
        return
    try:
        with (
            open(source_name, "r") as source_file,
            open(target_name, "w") as target_file,
        ):
            target_file.write(source_file.read())
    except FileNotFoundError:
        return
