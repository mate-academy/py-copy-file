def copy_file(command: str) -> None:
    text = command.split()
    if len(text) == 3:
        if text[0] == "cp" and text[1] != text[2]:
            with (open(text[1], "r") as source,
                  open(text[2], "r") as destination):
                destination.write(source.read())
