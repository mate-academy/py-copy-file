def copy_file(command: str) -> None:
    temp = command.split(" ")
    old_file = temp[1]
    new_file = temp[2]
    if old_file == new_file:
        exit()
    with open(old_file, "r") as old:
        with open(new_file, "w") as new:
            new.write(old.read())
