def copy_file(command: str) -> None:
    orig_file, new_file = command[3:].split(" ")
    if orig_file == new_file:
        return
    with open(orig_file, "r") as f1, open(new_file, "w") as f2:
        for line in f1.readlines():
            f2.write(line)
