def copy_file(command: str) -> None:
    with open(command.split()[1] + ".txt", "r") as text_file,\
            open(command.split()[2], "w") as copy_text_file:
        content = text_file.read()
        copy_text_file.write(content)
