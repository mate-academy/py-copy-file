def copy_file(name: str) -> None:
    splited = name.split(" ")

    if len(splited) != 3 or splited[0] != "cp" or splited[1] == splited[2]:
        return

    try:
        with open(splited[1], "r") as file_in:
            text = file_in.read()

        with open(splited[2], "w") as file_out:
            file_out.write(text)
    except FileNotFoundError:
        return
