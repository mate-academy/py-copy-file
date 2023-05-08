def copy_file(command: str) -> None:
    files = command.split()
    with open(files[1], "r") as f_in, open(files[2], "w") as f_out:
        if f_in.name == f_out.name:
            return
        f_out.write(f_in.read())
