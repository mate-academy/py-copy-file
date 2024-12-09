def copy_file(command: str) -> None:
    f_name = command.split(" ")[1]
    d_file = command.split(" ")[2]
    if f_name == d_file:
        return None
    with open(f_name, "r") as fro, open(d_file, "w") as dest:
        dest.write(fro.read())
