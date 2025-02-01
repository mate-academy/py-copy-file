def copy_file(command: str) -> None:
    linux = command.split()
    if len(linux) == 3:
        if linux[0] != "cp":
            raise ValueError
        if linux[1] == linux[-1]:
            raise ValueError
        with open((f"{linux[1]}"), "r") as src, open((f"{linux[-1]}"), "w") as dst:
            dst.write(src.read())
