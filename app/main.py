def copy_file(command: str) -> None:
    split = command.split()
    if (len(split) == 3
            and split[0] == "cp"
            and split[1] != split[2]):
        with open(split[1]) as content, open(split[2], "w") as new_file:
            new_file.write(content.read())
