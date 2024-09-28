def copy_file(command: str) -> None:
    command_name, first_file, second_file = command.split()
    if command_name == "cp" and first_file != second_file:
        with open(first_file, "r") as first, open(second_file, "w") as second:
            second.write(first.read())
