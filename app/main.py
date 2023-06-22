def copy_file(command: str) -> None:
    list_words = command.split()
    if list_words[1] != list_words[2]:
        with open(list_words[1], "r") as file_in, \
                open(list_words[2], "w") as file_out:
            content_file = file_in.read()
            file_out.write(content_file)
