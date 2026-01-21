def copy_file(command: str) -> None:
    ls = command.split(" ")
    if len(ls) == 3 and ls[0] == "cp":
        try:
            fil1 = ls[1]
            fil2 = ls[2]
            with open(fil1, "r") as fill1, open(fil2, "w") as fill2:
                for line in fill1:
                    fill2.write(line)
        except Exception:
            return
    else:
        return
