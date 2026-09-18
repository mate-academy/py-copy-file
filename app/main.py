def copy_file(command: str) -> None:
    if len(command) != 0:
        line = command.split(" ")
    else:
        return 0

    if len(line) == 3 and line[0] == "cp" and line[1] != line[2]:
        try:
            with open(line[1], "r") as f:
                file_in = f.read()
                with open(line[2], "w") as f2:
                    f2.write(file_in)
        except FileNotFoundError:
            return 0
