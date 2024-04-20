def copy_file(text: str) -> None:
    text = text.split()
    if len(text) != 3 or text[0] != "cp" or text[1] == text[2]:
        raise Exception("Wrong command")
    with open(text[2], "r") as file_in, open(text[1], "w") as file_out:
        file_out.write(file_in.read())
