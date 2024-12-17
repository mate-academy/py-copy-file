def copy_file(command: str) -> None:
    f_in = command.split(" ")[1]
    f_out = command.split(" ")[2]
    if f_in == f_out:
        return None
    with open(f_in, "r") as file_in, open(f_out, "w") as file_out:
        info = file_in.read()
        file_out.write(info)
