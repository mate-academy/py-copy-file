def copy_file(command: str) -> None:
    text = command.split()
    if text[0] != "cp" or text[1] == text[2]:
        return
    with open(text[1], "r") as file1, open(text[2], "w") as file2:
        file2.write(file1.read())
