def copy_file(command: str) -> None:
    words = command.split()

    if words[1] == words[2]:
        return

    with open(words[1]) as file_in, open(words[2], "w") as file_out:
        content = file_in.read()

        file_out.write(content)
