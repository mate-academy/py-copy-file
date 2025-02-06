def copy_file(command: str) -> None:
    ls = command.split()
    first = ls[1]
    second = ls[2]
    if not first == second:
        with open(first, "r") as one, open(second, "w") as two:
            two.write(one.read())
