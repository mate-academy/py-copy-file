def copy_file(file_names: str) -> None:
    command, original, copy = file_names.split()
    if command == "cp" and original != copy:
        with open(original, "r") as original, open(copy, "w") as copy:
            copy.writelines(original.readlines())
