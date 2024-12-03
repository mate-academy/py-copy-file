def copy_file(command: str) -> None:
    words = command.split()
    word1 = words[1]
    word2 = words[2]

    if word1 == word2:
        return

    with open(word1, "r") as file1, open(word2, "w") as file2:
        file2.write(file1.read())
