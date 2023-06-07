def copy_file(command: str) -> None:
    command = command.split(" ")
    file = command[1]
    copy_file = command[2]
    if file == copy_file:
        return
    with open(file, "r") as original, open(copy_file, "w") as copy:
        copy.write(original.read())
