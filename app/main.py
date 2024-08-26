def copy_dile(command: str) -> None:
    cp, old, new = command.split()
    if cp == "cp" and old != new:
        with open(old, "r") as old, open(new, "w") as new:
            for line in old.readlines():
                new.write(line)
