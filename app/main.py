def copy_file(command: str) -> None:
    """ Copy content from one file to another
    if given file names are different. """

    _, copy, paste = command.split()

    if copy != paste:
        with (open(copy) as from_file,
              open(paste, "w") as paste_file):
            paste_file.write(from_file.read())


if __name__ == "__main__":
    copy_file("cp test.txt test1.txt")
    print(open("test.txt").read() == open("test1.txt").read())
