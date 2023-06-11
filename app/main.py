def copy_file(command: str) -> None:
    words = command.split(" ")

    if words[1] == words[2]:
        return

    with open(words[1], "r") as old_file:
        with open(words[2], "w") as new_file:
            content = old_file.read()
            new_file.write(content)
