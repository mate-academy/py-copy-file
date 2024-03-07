def copy_file(commdand: str) -> None:
    splitted_file = commdand.split()
    if len(splitted_file) != 3:
        return
    command, file_from, file_to = splitted_file
    if command != "cp":
        return
    if file_from == file_to:
        return

    with open(file_from, "r") as file_from, open(file_to, "w") as file_to:
        file_to.write(file_from.read())
