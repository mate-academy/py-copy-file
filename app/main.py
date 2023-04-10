def copy_file(command: str) -> None:
    if len(command.split()) != 3 or command.split()[0] != "cp":
        return
    first_file = command.split()[1]
    second_file = command.split()[2]
    if first_file != second_file:
        with open(first_file, "r") as old_file, \
                open(second_file, "w") as new_file:
            text_to_copy = str(old_file.read())
            new_file.write(text_to_copy)
