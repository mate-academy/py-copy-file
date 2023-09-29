def copy_file(command: str) -> None:
    separate = command.split()
    old_file = separate[1]
    new_file = separate[2]
    if old_file == new_file:
        return
    with open(old_file, "r") as f, open(new_file, "w") as new_f:
        data = f.readlines()
        for row in data:
            new_f.write(row)
