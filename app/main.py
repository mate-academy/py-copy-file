def copy_file(command: str) -> None:
    mode, s_file, d_file = command.split()
    if mode == "cp" and s_file != d_file:
        with open(s_file, "r") as file_in, open(d_file, "w") as file_out:
            file_out.write(file_in.read())
