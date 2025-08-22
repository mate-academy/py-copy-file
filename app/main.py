def copy_file(command: str) -> None:
    parts = command.split()

    if parts[:1] != ["cp"] or len(parts) != 3:
        return

    _, source_file_name, target_file_name = parts

    if source_file_name == target_file_name:
        return

    try:
        with (open(source_file_name, "r") as source_file_object,
              open(target_file_name, "w") as target_file_object):
            target_file_object.write(source_file_object.read())
    except FileNotFoundError:
        pass
