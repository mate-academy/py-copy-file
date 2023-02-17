def copy_file(command: str):
    res = command.split(" ")
    if res[0] == "cp":
        with open(res[1], "r") as source:
            data = source.read()

        with open(res[2], "w") as target:
            target.write(data)
