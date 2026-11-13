def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    cmd, source_name, target_name = parts
    if cmd != "cp" or source_name == target_name:
        return

    try:
        with open(source_name, "r") as file_in:
            content = file_in.read()
    except FileNotFoundError:
        return

    with open(target_name, "w") as file_out:
        file_out.write(content)
