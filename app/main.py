def copy_file(command: str) -> None:
    list_command = list(command)
    word = []
    for index, bykva in enumerate(list_command):
        if index >= 3:
            if bykva == " ":
                old_name = "".join(word)
                word = []
            else:
                word.append(bykva)
    new_name = "".join(word)
    if new_name != old_name:
        with open(new_name, "w") as new_file, open(old_name, "r") as old_file:
            new_file.write(old_file.read())
