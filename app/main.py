def copy_dile(command: str) -> None:
    if len(command.split()) == 3:
        cp, old, new = command.split()
    if cp == "cp" and old != new:
        with open(old, "r") as old, open(new, "w") as new:
            new.write(old.read())
