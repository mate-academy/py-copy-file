def copy_file(command: str) -> None:
    text = command.split()
    if len(text) == 3 and text[0] == "cp" and text[1] != text[2]:
        with (open(text[1], "r") as file_in,
              open(text[2], "w") as file_copy):
            content = file_in.read()
            file_copy.write(content)
