def copy_file(command: str) -> None:
    files = command.split()
    if len(files) < 3 or files[0] != "cp" or files[1] == files[2]:
        return
    try:
        with open(files[1], "r") as original, open(files[2], "w") as copy:
            for line in original:
                copy.write(line)
    except FileNotFoundError:
        return
