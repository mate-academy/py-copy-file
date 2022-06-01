def copy_file(command: str):
    parsed = command.split()
    if parsed[0] == "cp" and parsed[1] != parsed[2]:
        with open(parsed[1], "r") as f1, open(parsed[2], "w") as f2:
            f2.write(f1.read())
