def copy_file(command: str) -> None:
    command = command.split()
    cp = command[0]
    old_file = command[1]
    new_file = command[2]
    if cp == "cp" and old_file != new_file:
        with open(old_file, "r") as old_file, open(new_file, "w") as new_file:
            new_file.write(old_file.read())
