def copy_file(command: str) -> None:
    try:
        if not command:
            return
        split_string = command.split()

        if len(split_string) != 3 or split_string[0] != "cp":
            return
        origin, rep = split_string[1], split_string[2]

        if origin == rep:
            return

        with open(origin, "r") as ori, open(rep, "w") as re:
            re.write(ori.read())
    except FileNotFoundError:
        pass
