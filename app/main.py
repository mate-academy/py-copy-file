def copy_file(command: str) -> None:
    files = command.split(" ")
    if files[0] != "cp" or files[1] == files[2]:
        return
    with open(files[1], "r") as first, open(files[2], "w") as second:
        second.write(first.read())
