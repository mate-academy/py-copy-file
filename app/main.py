def copy_file(command: str) -> None:
    command_lst = command.split()
    if len(command_lst) != 3:
        return
    cp, old_file_name, new_file_name = command_lst

    if cp != "cp":
        return
    if old_file_name == new_file_name:
        return

    try:
        with (open(old_file_name, "r") as old_file,
              open(new_file_name, "w") as new_file):
            new_file.write(old_file.read())
    except FileNotFoundError:
        return
