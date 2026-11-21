def copy_file(command: str) -> None:
    try:
        cp, original, copy = command.split()
        if original == copy or cp != "cp":
            return
        with open(original, "r") as original_file, open(copy, "w") as copied_file:
            copied_file.write(original_file.read())
    except (FileNotFoundError, ValueError):
        return
