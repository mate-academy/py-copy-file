def copy_file(command: str) -> None:
    file_copy = command[1]
    new_file = command[2]

    if file_copy == new_file:
        return

    with open(file_copy, "r") as copy, open(new_file, "w") as file:
        file.write(copy.read())
