def copy_file(command: str) -> None:
    separate = command.split()
    if len(separate) == 3:
        if separate[0] == "cp":
            old_file = separate[1]
            new_file = separate[2]
    if old_file == new_file:
        return
    with open(old_file, "r") as old_f, open(new_file, "w") as new_f:
        data = old_f.readlines()
        for row in data:
            new_f.write(row)
