def copy_file(command: str) -> None:
    first_file = command.split()[1]
    second_file = command.split()[2]
    if first_file != second_file:
        with (open(first_file) as copied_file,
                open(second_file, "w") as pasted_file):
            pasted_file.write(copied_file.read())
