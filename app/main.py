def copy_file(command: str) -> None:
    files = command.split(" ")
    if files[1] == files[2] or files[0] != "cp":
        return
    with open(files[1], "r") as file_in, open(files[2], "w") as file_out:
        file_out.write(file_in.read())
