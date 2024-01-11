def copy_file(text: str) -> None:
    if len(text.split()) == 3:
        text = text.split()
        if text[0] == "cp" and text[1] != text[2]:
            with open(text[1], "r") as file_in, open(text[2], "w") as file_out:
                file_out.write(file_in.read())
