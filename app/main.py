def copy_file(command: str) -> None:
    linux = command.split()
    if linux != "cp":
        raise ValueError
    if linux[1] == linux[-1]:
        pass
    with open("source.txt", "r") as src, open("destination.txt", "w") as dst:
        dst.write(src.read())
