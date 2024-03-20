def copy_file(command: str) -> None:
    names = command.split()
    if len(names) != 3:
        return
    cp, old_file_name, new_file_name = names
    if old_file_name != new_file_name and cp == "cp":
        with (open(old_file_name, "r") as old_file,
              open(new_file_name, "w") as new_file):
            new_file.write(old_file.read())
