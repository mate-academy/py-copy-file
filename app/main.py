def copy_file(text: str) -> None:
    text = text.split()
    if len(text) == 3 and text[1] == text[2]:
        print("Does nothing")
    if len(text) == 3 and text[1] != text[2]:
        open(text[2], "w").write(open(text[1], "r").read())
