def copy_file(command: str) -> None:
    split_cmd = command.split()
    if len(split_cmd) < 3:
        print("Invalid value")
        return

    if split_cmd[1] != split_cmd[2]:
        with open(split_cmd[1], 'r') as r, open(split_cmd[2], "a") as w:
            w.write(r.read())
