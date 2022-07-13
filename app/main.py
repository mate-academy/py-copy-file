def copy_file(command: str):
    names = command.split()

    if names[1] != names[2]:
        with open(names[1], "r") as f_in, open(names[2], "w") as f_out:
            f_out.write(f_in.read())
