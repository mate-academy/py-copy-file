def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    command_name, source, target = parts
    if command_name != "cp" or source == target:
        return

    try:
        with open(source, "r") as file_in, open(target, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return
