def copy_file(command: str) -> None:
    parts = command.split(' ', 2)

    if len(parts) != 3 or parts[0] != "cp":
        return

    _, src, dst = parts

    if src == dst:
        return

    try:
        with open(src, "r", encoding="utf-8") as source_file_object, \
             open(dst, "w", encoding="utf-8") as destination_file_object:
            destination_file_object.write(source_file_object.read())
    except FileNotFoundError:
        return
