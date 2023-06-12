def copy_file(command: str) -> None:
    cp, first_file, second_file = command.split()

    if first_file != second_file:
        with open(first_file, "r") as old, open(second_file, "w") as new:
            content = old.read()
            new.write(content)
