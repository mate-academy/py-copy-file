def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return
    if parts[0] != "cp":
        return
    old_file = parts[1]
    new_file = parts[2]
    if old_file == new_file:
        return
    try:
        with open(old_file, "r") as file_in, open(new_file, "w") as file_out:
            content = file_in.read()
            file_out.write(content)
    except FileNotFoundError:
        return
