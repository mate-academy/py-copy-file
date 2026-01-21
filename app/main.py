def copy_file(command: str) -> None:
    file = command.split()
    if file[1] != file[2] and file[0] == "cp":
        with open(file[1], "r") as origin, open(file[2], "w") as copy:
            copy.write(origin.read())
