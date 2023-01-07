def copy_file(command: str) -> None:
    original = command.split()[1]
    copy = command.split()[2]
    if original == copy:
        return
    with open(original, "r") as original, open(copy, "w") as copy:
        copy.write(original.read())
