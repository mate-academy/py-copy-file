def copy_file(command: str = "cp file.txt file.txt") -> None:
    try:
        cp, fname1, fname2 = command.split()
    except ValueError:
        return None
    if cp != "cp" or fname1 == fname2:
        return None
    try:
        with open(fname1, "r") as fn1, open(fname2, "w") as fn2:
            fn2.write(fn1.read())
    except FileNotFoundError:
        return None


if __name__ == "__main__":
    pass
