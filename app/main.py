def copy_file(command: str) -> None:
    cp, origin, copy = command.split()

    if origin == copy or cp == "cp":
        return None

    with (
        open(origin, "r") as origin,
        open(copy, "w") as copy
    ):
        copy.write(origin.read())
