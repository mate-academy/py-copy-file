def copy_file(command: str) -> None:
    if len(command.split()) < 3:
        return
    command_name = command.split()[0]
    if command_name != "cp":
        return
    original_file = command.split()[1]
    copied_file = command.split()[2]
    if original_file == copied_file:
        return
    try:
        with open(original_file) as f_original, open(copied_file, "w") as f_copied:
            f_copied.write(f_original.read())
    except FileNotFoundError:
        return
