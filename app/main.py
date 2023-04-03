def copy_file(command: str) -> None:
    sp_com = command.split()
    if sp_com[0] == "cp" and sp_com[1] != sp_com[2]:
        with open(sp_com[1], "r") as file_in, open(sp_com[2], "w") as file_out:
            file_out.write(file_in.read())
