def copy_file(command: str) -> None:
    ls = command.split(" ")
    if ls[1] == ls[2]:
        return
    with open(ls[1], "r") as file_in, open(ls[2], "w") as file_out:
        file_out.write(file_in.read())
