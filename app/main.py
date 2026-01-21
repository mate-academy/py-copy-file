def copy_file(command: str) -> None:
    if not command.startswith("cp "):
        return

    parts = command.split()
    if len(parts) != 3:
        return

    _, source, dest = parts

    if source == dest:
        return

    try:
        with open(source, "rb") as file_in, open(dest, "wb") as file_out:
            file_out.write(file_in.read())
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        return
