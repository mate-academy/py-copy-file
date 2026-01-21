def copy_file(command: str) -> None:
    short_command = command.split()[0]
    original = command.split()[1]
    copy = command.split()[2]
    if short_command != "cp" or original == copy:
        return
    with open(original, "r") as original, open(copy, "w") as copy:
        copy.write(original.read())
