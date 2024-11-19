def copy_file(command: str) -> None:
    name = command.split()

    with open(name[1], "r") as file_in, open(name[2], "w") as file_out:
        if name[1] == name[2]:
            return
        for line in file_in:
            file_out.write(line)
