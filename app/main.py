def copy_file(command: str) -> None:
    line = command.split()
    if len(line) == 3 and line[0] == "cp" and not line[1] == line[2]:
        with open(line[1], "r") as file_in, open(line[2], "w") as file_out:
            file_out.write(file_in.read())
