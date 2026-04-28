def copy_file(command: str) -> None | bool:
    words = command.split()
    if len(words) != 3:
        return None
    try:
        open(words[1], "r")
    except FileNotFoundError:
        return None
    if words[1] == words[2]:
        return None
    elif words[0] != "cp":
        return None
    else:
        with open(words[1], "r") as f1, open(words[2], "w") as f2:
            f2.write(f1.read())
            return True
