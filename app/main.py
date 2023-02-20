def copy_file(file_names: str) -> None:
    command, original, copy = file_names.split()
    if original == copy:
        exit(0)
    if command == "cp":
        with open(original, "r") as original, open(copy, "w") as copy:
            lines = original.readlines()
            copy.writelines(lines)
