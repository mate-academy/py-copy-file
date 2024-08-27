def copy_dile(command: str) -> None:
    _command = command.split()
    if len(_command) == 3:
        cp, old, new = _command
    if cp == "cp" and old != new:
        with open(old, "r") as old, open(new, "w") as new:
            new.write(old.read())
