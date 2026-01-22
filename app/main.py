def copy_file(command: str) -> None:
    parts = command.split(" ")
    if len(parts) != 3:
        return
    file_command, old_file_name, new_file_name = parts

    if old_file_name == new_file_name or file_command != "cp":
        return

    try:
        with (open(old_file_name, "r") as old_file,
              open(new_file_name, "w") as new_file):
            new_file.write(old_file.read())
    except FileNotFoundError:
        return
