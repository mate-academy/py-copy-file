def copy_file(command: str) -> None:
    command, original_file, file_to_copy = command.split()

    if not (len(command.split()) < 3
            or original_file == file_to_copy
            or command != "cp"):

        with open(original_file, "r") as orig, open(file_to_copy, "a") as copy:
            copy.write(orig.read())
