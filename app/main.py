def copy_file(command: str) -> None:
    old_file, new_file = (command[2:].split())
    if old_file != new_file:
        with open(old_file, "r") as file:
            info = file.read()
        with open(new_file, "w") as my_file:
            my_file.write(info)
