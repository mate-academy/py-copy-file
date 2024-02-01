def copy_file(command: str) -> None:
    command_text, source, new_file = command.split()
    if command_text == "cp" and source != new_file:
        with open(source, "r") as source, open(new_file, "w") as new_file:
            new_file.write(source.read())
