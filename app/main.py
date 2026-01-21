def copy_file(command: str) -> None:
    command = command.split()
    if command[0] == "cp" and command[1] != command[2]:
        with open(command[1]) as f, open(command[2], "w") as copy:
            copy.write(f.read())
