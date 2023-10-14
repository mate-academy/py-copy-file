def copy_file(command: str) -> None:
    vul = command.split()
    if vul[1] == vul[2] and vul[0] == "cp":
        return
    with open(vul[1], "r") as file_in, open(vul[2], "w") as file_out:
        file_out.write(file_in.read())
