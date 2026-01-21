def copy_file(command: str) -> None:
    list_words = command.split()
    if len(list_words) != 3 or list_words[0] != "cp":
        return
    if list_words[1] != list_words[2]:
        with (
            open(list_words[1], "r") as file_old,
            open(list_words[2], "w") as file_copy
        ):
            content = file_old.read()
            file_copy.write(content)
