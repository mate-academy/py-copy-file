def copy_file(command: str) -> None:
    name = command.split()[1:]
    if name[0] != name[1]:
        with open(name[0], "r") as file_in, open(name[1], "w") as file_out:
            file_out.write(file_in.read())
