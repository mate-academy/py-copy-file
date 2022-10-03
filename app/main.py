def copy_file(command: str):
    lst_separated = command.split(" ")
    if lst_separated[0] != "cp" or lst_separated[1] == lst_separated[2]:
        return

    with open(lst_separated[1], "r") as f, open(lst_separated[2], "a") as s:
        for line in f:
            s.write(line)
