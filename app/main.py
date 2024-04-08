def copy_file(command: str) -> None:
    if len(command) != 3:
        return

    command, first_file, second_file = command.split()

    if command != "cp" or first_file == second_file:
        return

    with (
        open(first_file, "r") as initial_file,
        open(second_file, "w") as file_copy
    ):
        file_copy.write(initial_file.read())
