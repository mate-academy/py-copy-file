def copy_file(command: str) -> None:
    if command.count(" ") == 2:
        command, old_file, new_file = command.split()
        if old_file != new_file:
            with open(new_file, "w") as f_1, open(old_file, "r") as f_2:
                f_1.write(f_2.read())
