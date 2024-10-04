def copy_file(command: str) -> None:
    first_file = command.split(" ")[1]
    second_file = command.split(" ")[2]

    if first_file == second_file:
        return

    with open(first_file, "r") as first, open(second_file, "w") as second:
        second.write(first.read())
