def copy_file(command: str) -> None:
    name = command.split()
    if (name[0] == "cp"
            and name[1] != name[2]):
        with open(name[1], "r") as origin:
            content = origin.read()
        with open(name[2], "w") as copy:
            copy.write(content)
