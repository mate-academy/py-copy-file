def copy_vile(command: str) -> None:
    text = command.split()
    if text[0] == "cp" and text[1] != text[2]:
        with (
            open(text[1], "r") as source,
            open(text[2], "w") as new_file
        ):
            new_file.write(source.read())
