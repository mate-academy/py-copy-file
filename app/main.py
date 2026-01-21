def copy_file(cp_cmd: str) -> None:
    arg = cp_cmd.split(" ")
    if arg[0] != "cp" or arg[1] == arg[2]:
        return
    with open(arg[1], "r") as file_in, open(arg[2], "w") as file_out:
        content = file_in.read()
        file_out.write(content)
