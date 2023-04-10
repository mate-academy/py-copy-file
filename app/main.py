def copy_file(command: str) -> None:
    listed_command = command.split()
    first_file = listed_command[1]
    second_file = listed_command[2]
    if first_file != second_file and len(listed_command) == 3:
        with open(first_file, "r") as old_file, \
                open(second_file, "w") as new_file:
            text_to_copy = str(old_file.read())
            new_file.write(text_to_copy)


