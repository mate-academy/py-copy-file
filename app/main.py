def copy_file(file_names: str) -> None:
    command, original, copy = file_names.split()
    if command != "cp":
        exit(f"Command '{command}' was not found")
    if original == copy:
        exit(0)
    with open(original, "r") as original, open(copy, "w") as copy:
        lines = original.readlines()
        copy.writelines(lines)
