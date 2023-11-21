def copy_file(command: str) -> None:
    part = command.split()
    if not part[0].startswith("cp"):
        return
    if part[1] != part[2]:
        with open(part[1], "r") as origin_file, open(part[2], "w") as cp_file:
            cp_file.write(origin_file.read())
