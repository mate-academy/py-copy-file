def copy_file(command: str) -> None:
    if (
        not command.startswith("cp ")
        or command.count(" ") != 2
        or command.count(".txt") != 2
    ):
        return None
    cp, name1, name2 = command.split(" ")
    if name1 == name2:
        return None
    else:
        try:
            with open(name1, "r") as f_in, open(name2, "w") as f_out:
                for line in f_in:
                    f_out.write(line)
        except FileNotFoundError:
            return None
