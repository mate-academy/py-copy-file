def copy_file(command: str) -> None:
    words = command.split()

    if len(words) != 3 or words[0] != "cp":
        return

    file_from, file_to = words[1:]

    if file_from == file_to:
        return

    try:
        with open(file_from, "r") as f_from, open(file_to, "w") as f_to:
            from_content = f_from.read()
            f_to.write(from_content)
    except FileNotFoundError:
        return
