def copy_file(command: str) -> None:
    names = command.split(" ")

    if len(names) != 3 or names[0] != "cp":
        return

    _, origin, destine = names

    if origin == destine:
        return

    try:
        with open(origin, "r") as file_in, open(destine, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
