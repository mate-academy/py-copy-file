def copy_file(command: str) -> None:
    line = command.split()
    if line[0] == "cp":
        if not line[1] == line[2]:
            with open(line[1], "r") as file_in, open(line[2], "w") as file_out:
                file_out.write(file_in.read())
