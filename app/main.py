def copy_file(command: str) -> None:
    result = command.split(" ")
    file = result[1]
    copy_of_file = result[2]
    if result[0] != "cp":
        return
    if file == copy_file:
        return

    with open(file, "rt") as origin, open(copy_of_file, "w") as copy:
        copy.write(origin.read())
