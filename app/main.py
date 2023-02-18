def copy_file(command: str) -> None:
    temp = command.split(" ")
    if temp[0] != "cp":
        return 0
    if temp[1] == temp[2]:
        return 0
    with open(f"{temp[1]}", "r") as source, open(f"{temp[2]}", "w") as copy:
        copy.write(source.read())
