def copy_file(command: str) -> None:
    cp, file, new_file = command.split()
    if cp == "cp" and file != new_file:
        with open(file, "r") as original_file, \
                open(new_file, "w") as file_copy:
            file_copy.write(original_file.read())
