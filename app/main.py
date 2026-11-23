def copy_file(command: str) -> None:
    if not command.startswith("cp"):
        return None
    text = command.split()
    try:
        if text[1] == text[2]:
            return None
    except IndexError:
        return None
    try:
        with open(text[1], "r") as read_file, open(text[2], "w") as write_file:
            write_file.write(read_file.read())
    except FileNotFoundError:
        return None
