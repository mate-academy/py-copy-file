def copy_file(command: str):
    old_file = command.split()[1]
    new_file = command.split()[2]
    if old_file != new_file:
        with open(old_file, "r") as file_old:
            with open(new_file, "w") as file_new:
                file_new.write(file_old.read())
