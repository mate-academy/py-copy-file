def copy_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3:
        return

    cmd, source_file_name, dest_file_name = parts

    if cmd != "cp":
        return

    if source_file_name == dest_file_name:
        return

    try:
        with open(source_file_name, "r") as file_in, open(dest_file_name, "w") as file_out:
            text_to_copy = file_in.read()
            file_out.write(text_to_copy)
    except FileNotFoundError:
        return
