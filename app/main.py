def copy_file(command: str) -> None:
    text = command.split()
    if len(text) != 3 or text[1] == text[2] or text[0] != "cp":
        return None
    plik1 = text[1]
    plik2 = text[2]
    try:
        with open(plik1, "r") as file:
            value = file.read()
            with open(plik2, "w") as file2:
                file2.write(value)
    except FileNotFoundError:
        return None
