def copy_file(command: str) -> None:
    """ Copy content from one file to another
    if given file names are different. """

    mode, copy, paste = command.split()

    if copy != paste and mode == "cp":
        with (open(copy) as from_file,
              open(paste, "w") as paste_file):
            paste_file.write(from_file.read())
