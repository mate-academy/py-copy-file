def copy_file(command: str) -> None:
    names = command.split(" ")

    if len(names) != 3 or names[0] != "cp":
        return

    _, origin, destine = names

    try:
        with open(origin, "r") as origin, open(destine, "w") as destine:
            destine.write(origin.read())
    except FileNotFoundError:
        return
