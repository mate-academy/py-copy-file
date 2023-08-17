def copy_file(command: str) -> None:
    files_names = command.split(" ")
    first_file, second_file = files_names[1], files_names[2]

    if first_file == second_file:
        return

    with open(first_file, "r") as original, open(second_file, "w") as copied:
        copied.write(original.read())
