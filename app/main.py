def copy_file(command: str) -> None:
    x = command.split()
    comm = x[0]
    first_file = x[1]
    second_file = x[2]
    if first_file != second_file:
        with open(first_file, "r") as first,\
            open(second_file, "w") as second:
            y = str(first.read())
            second.write(y)
