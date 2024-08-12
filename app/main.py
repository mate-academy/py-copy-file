def copy_file(command: str) -> None:
    command = command.split()
    if command[1] == command[2]:
        pass
    else:
        with open(command[1], "r") as f, open(command[2], "w") as f_copy:
            f_copy.write(f.read())
