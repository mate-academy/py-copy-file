def copy_file(values: str) -> None:
    value = values.split(" ")
    if value[0] != "cp":
        return None
    if value[1] == value[2]:
        return None
    if open(value[1], "r").read() == open(value[2], "r").read():
        return None
    else:
        with open(value[1], "r") as file, open(value[2], "w") as file:
            data = file.read()
            file.write(data)
        return None
