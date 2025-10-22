def copy_file(command: str) -> None:

    list_of_words = command.split()
    if len(list_of_words) != 3 or list_of_words[0] != "cp":
        return

    source = list_of_words[1]
    target = list_of_words[2]

    if source == target:
        return
    try:
        with open(source, "r") as file_in, open(target, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
