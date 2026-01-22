def copy_file(command: str) -> None:
    cp, filename, new_filename = command.split(" ")
    if not filename == new_filename:
        with open(filename, "r") as first_file:
            with open(new_filename, "a") as second_file:
                for line in first_file:
                    second_file.write(line)
