def copy_file(command: str) -> None:
    split_command = command.split()
    if len(split_command) < 3:
        print("Invalid value")
        return
    if split_command[1] != split_command[2]:
        with open(split_command[1], 'r') as r, open(split_command[2], "a") as w:
            w.write(r.read())
