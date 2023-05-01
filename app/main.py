def copy_file(command: str) -> None:
    cp, old_file, new_file = command.split(" ")
    if cp == "cp" and old_file != new_file:
        with open(old_file, "r") as old, open(new_file, "w") as new:
            new.write(old.read())
