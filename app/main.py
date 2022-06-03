def copy_file(command: str):
    file = command.split()
    if file[1] != file[2] and file[0] == "cp":
        with open(file[1], "r") as start_f, open(file[2], "w") as end_f:
            end_f.write(start_f.read())
