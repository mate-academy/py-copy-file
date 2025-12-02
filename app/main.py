def copy_file(command: str) -> None:
    parts = command.split(" ")

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, source_path, dest_path = parts

    if source_path == dest_path:
        return

    try:
        with open(source_path, "r") as source_file, \
             open(dest_path, "w") as destination_file:

            content = source_file.read()
            destination_file.write(content)

    except FileNotFoundError:
        pass
