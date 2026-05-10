def copy_file(command: str) -> None:
    word = command.split(" ")
    if len(word) != 3 or word[0] != "cp":
        return
    if word[1] == word[2]:
        return
    try:
        with open(word[1]) as f:
            with open(word[2], "w") as new_file:
                for line in f:
                    new_file.write(line)
    except FileNotFoundError:
        return
