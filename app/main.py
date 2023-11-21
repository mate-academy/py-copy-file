
def copy_file(command: str) -> None:
    file = command.split()
    if not file[0].startswith("cp"):
        return
    if file[1] != file[2]:
        with open(file[1], "r") as origin_file, open(file[2], "w") as cp_file:
            cp_file.write(origin_file.read())
