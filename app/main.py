def copy_file(command: str) -> None:
    splitted = command.split()
    if len(splitted) < 3:
        return
    if splitted[0] != "cp":
        return
    name_of_file = splitted[1]
    name_of_new_file = splitted[2]
    if name_of_file == name_of_new_file:
        return

    try:
        with (open(name_of_file, "r") as src,
              open(name_of_new_file, "w") as dst):
            content = src.read()
            dst.write(content)
    except FileNotFoundError:
        return
