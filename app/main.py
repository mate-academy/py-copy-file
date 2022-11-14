def copy_file(command: str) -> None:
    ls = command.split()
    if len(ls) == 3:
        with open(ls[1], "r") as file_in, open(ls[2], "w") as file_out:
            file_out.writelines(file_in.readlines())
