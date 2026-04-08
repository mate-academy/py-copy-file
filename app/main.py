def copy_file(command: str) -> None:

    result = command.split()

    if len(result) != 3 or result[0] != "cp":
        return

    if result[1] == result[2]:
        return
    else:
        try:
            with open(result[1], "r") as fi_in, open(result[2], "w") as fi_n:
                fi_n.write(fi_in.read())
        except OSError:
            return
