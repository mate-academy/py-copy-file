def copy_file(command: str) -> None:
    list_of_words = command.split()
    if list_of_words[1] == list_of_words[2]:
        return
    elif list_of_words[1] != list_of_words[2]:
        with open(list_of_words[1], "r") as file_in:
            content = file_in.read()
            file_in.close()
        with open(list_of_words[2], "w") as file_out:
            file_out.write(content)
            file_out.close()
