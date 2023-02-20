def copy_file(command: str) -> None:
    result = command.split(" ")
    if result[0] == "cp":
        with open(result[1], "r") as source, open(result[2], "w") as target:
            data = source.read()
            target.write(data)
