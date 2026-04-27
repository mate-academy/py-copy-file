def copy_file(command: str) -> None:
    parts = command.split()

    if len(parts) != 3:
        return

    cmd, source_file, new_file = parts

    if cmd != "cp":
        return

    if source_file == new_file:
        return

    try:
        with (open(source_file, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
