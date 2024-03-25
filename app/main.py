def copy_file(text: str) -> None:
    text = text.split()
    if len(text) == 3:
        command, source, copy = text
        if command == "cd" and source != copy:
            with open(source, "r") as source, open(copy, "w") as copy:
                copy.write(source.read())
