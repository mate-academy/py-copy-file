def copy_file(command: str) -> None:
    wrd = command.split()
    if len(wrd) == 3 and wrd[0] == "cp":
        if wrd[1] != wrd[2]:
            try:
                with open(wrd[1], "r") as f_in, open(wrd[2], "w") as f_out:
                    inside_of_file = f_in.read()
                    f_out.write(inside_of_file)
            except FileNotFoundError:
                pass
