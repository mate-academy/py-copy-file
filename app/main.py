def copy_file(command: str) -> None:
    parts = command.split()

    if parts[:1] != ["cp"] or len(parts) != 3:
        return

    _, source_file, target_file = parts

    if source_file == target_file:
        return

    try:
        with (open(source_file, "rb") as src_file,
              open(target_file, "wb") as dst_file):
            dst_file.write(src_file.read())
    except FileNotFoundError:
        pass
