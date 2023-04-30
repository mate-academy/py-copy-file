def copy_file(command: str) -> None:
    copy = command.split()
    if len(copy) != 3 and copy[0] != "cp" and copy[1] == copy[2]:
        return
    with open(copy[1], "r") as file_in, open(copy[2], "w") as file_out:
        file_out.write(file_in.read())
