def copy_file(command: str) -> None:
    cs = command.split()
    if cs[0] == "cp" and cs[1] != cs[2]:
        with open(cs[1], "r") as file_out, open(cs[2], "w") as file_in:
            file_in.write(file_out.read())
