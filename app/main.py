def copy_file(command: str) -> None:
    try:
        tokens = command.split(" ")
        if tokens[0] != "cp":
            return
        if tokens[1] == tokens[2]:
            pass
        else:
            with open(tokens[1], "r") as f, open(tokens[2], "w") as nf:
                nf.write(f.read())
    except FileNotFoundError:
        pass
    except IndexError:
        pass
