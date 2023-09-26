def copy_file(command: str) -> None:
    name1 = command.split()[1]
    name2 = command.split()[2]
    with open(name1) as f1, open(name2, "w") as f2:
        f2.write(f1.read())
