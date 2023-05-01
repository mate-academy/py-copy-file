def copy_file(command: str) -> None or str:
    try:
        cp, old_file, new_file = command.split(" ")
    except ValueError:
        return "invalid command"

    if cp != "cp":
        return "unknown command"

    if old_file != new_file:
        with open(old_file, "r") as copy_from, open(new_file, "w") as copy_to:
            copy_to.write(copy_from.read())
