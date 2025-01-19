def copy_file(command: str) -> None:
    files = command.split()[1:]
    with open(files[0], "r") as file:
        text_to_copy = file.read()
        with open(files[1], "w") as f:
            f.write(text_to_copy)
