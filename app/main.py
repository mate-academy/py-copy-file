def copy_file(command: str) -> None:
    cp, first_file, second_file = command.split(" ")

    if first_file != second_file:
        with open(first_file, "r") as old_file, \
                open(second_file, "w") as new_file:
            content = old_file.read()
            new_file.write(content)
    else:
        return
