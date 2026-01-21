def copy_file(command: str) -> None:
    try:
        command_cd, file_txt, new_file = command.split()
    except ValueError:
        return

    if file_txt == new_file or command_cd != "cp":
        return

    try:
        with open(file_txt, "r") as old, open(new_file, "w") as new:
            new.write(old.read())
    except FileNotFoundError:
        return
