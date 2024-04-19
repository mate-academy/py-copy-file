def copy_file(text: str):
    text = text.split()
    if "cp" in text[0] and text[1] == text[2]:
        print("Does nothing")
    if "cp" in text[0] and text[1] != text[2]:
        open(text[2], "w").write(open(text[1], "r").read())


