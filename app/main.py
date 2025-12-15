def copy_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) != 3:
        return
    action, original_file, copied_file = split_command
    if original_file == copied_file or action != "cp":
        return

    try:
        with (open(original_file, "rb") as file_in,
              open(copied_file, "wb") as file_out):
            file_out.write(file_in.read())
    except OSError:
        return
