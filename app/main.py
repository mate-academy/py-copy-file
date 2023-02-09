def copy_file(command: str) -> None:
    com = command.split()
    if com[1] != com[2]:
        with open(com[1], "r") as file_in, open(com[2], "w") as file_out:
            file_out.write(file_in.read())
