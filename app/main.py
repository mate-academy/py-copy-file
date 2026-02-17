def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    action, source_file, dest_file = parts
    if action != "cp" or source_file == dest_file:
        return

    try:
        with open(source_file, "r") as file_in, \
                open(dest_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
