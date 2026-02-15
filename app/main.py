def copy_file(some_file: str) -> None:
    if len(some_file.split()) < 3:
        return

    cp, old_file, new_file = some_file.split()

    if new_file == old_file or cp != "cp":
        return

    try:
        with open(old_file, "r") as old:
            source = old.read()
    except FileNotFoundError:
        return

    with open(new_file, "w") as new:
        new.write(source)
