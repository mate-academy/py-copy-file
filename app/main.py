def copy_file(command: str) -> None:
    text = command.split()
    if text[1] == text[2]:
        return

    with (
        open(text[1], "r") as file_in,
        open(text[2], "w") as file_copy
    ):
        file_copy.write(file_in.read())
