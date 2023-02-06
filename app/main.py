def copy_file(command: str) -> None:
    cp, start_file, next_file = command.split()
    if start_file != next_file and cp == "cp":
        with open(start_file, "r") as first_file, \
                open(next_file, "w") as second_file:
            text = first_file.read()
            second_file.write(text)
