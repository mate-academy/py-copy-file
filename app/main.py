def copy_file(command: str) -> None:
    ls_file = command.split()
    if ls_file[1] != ls_file[2] and ls_file[0] == "cp":
        with open(ls_file[1], "r") as old_file, open(ls_file[2], "w") as copy:
            copy.write(old_file.read())
