def copy_file(command: str) -> None:
    if command.split(" ")[1] != command.split(" ")[2]:
        with open(command.split(" ")[1], "r") as source:
            with open(command.split(" ")[2], "w") as copied_file:
                copied_file.write(source.read())
