def copy_file(command: str) -> None:
    text = command.split(" ")
    if text[0] != "cp":
        return
    if text[1] == text[2]:
        return
    with open(text[1], "r") as f1, open(text[2], "w") as f2:
        f2.write(f1.read())
