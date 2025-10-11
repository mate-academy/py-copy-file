def copy_file(command: str) -> None:
    if command:
        copy, paste = command[3:].split(" ")
        if copy != paste:
            with open(paste, "w") as pasted_file, open(copy) as copied_file:
                pasted_file.write(copied_file.read())
