def copy_file(command: str) -> None:
    origin_file = command.split()[1]
    file_copy = command.split()[2]
    if origin_file != copy_file:
        with open(origin_file, "r") as origin, open(file_copy, "w") as copy_f:
            for line in origin:
                copy_f.write(line)
