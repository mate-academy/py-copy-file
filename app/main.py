def copy_file(command: str):

    file = command.split()[1]
    copy = command.split()[2]

    if file != copy:
        with open(file, "r") as f:
            with open(copy, "w") as c:
                c.write(f.read())
