def copy_file(command: str) -> None:
    cmnd = command.split()
    if cmnd[1] == cmnd[2]:
        return
    with open(cmnd[1], "r") as file_in, open(cmnd[2], "w") as file_out:
        file_out.write(file_in.read())
