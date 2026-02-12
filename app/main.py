def copy_file(command: str) -> None:
    parts = command.strip().split()
    if len(parts) != 3 or parts[0] != "cp":
        return

    source_file = parts[1]
    dest_file = parts[2]
    if source_file == dest_file:
        return
    try:
        with (open(source_file, "rb") as source_file_obj,
              open(dest_file, "wb") as dest_file_obj):
            dest_file_obj.write(source_file_obj.read())
    except FileNotFoundError:
        return
