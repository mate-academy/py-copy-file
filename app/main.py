def copy_file(command: str) -> None:

    command = command.split()
    if len(command) == 3 and command[0] == "cp":
        if command[1] == command[2]:
            pass
        with open(command[1], "r") as f_in, open(command[2], "w") as f_out:
            f_out.write(f_in.read())
