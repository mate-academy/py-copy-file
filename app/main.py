def copy_file(command: str) -> None:
    operation, filename_from, filename_to = command.split()
    if filename_to == filename_from or operation != "cp":
        return

    with open(filename_from, "r") as file_from:
        with open(filename_to, "w") as file_to:
            file_to.write(file_from.read())
