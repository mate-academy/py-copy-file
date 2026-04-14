def copy_file(command: str) -> None:
    data = command.split()

    if len(data) != 3 or data[0] != "cp":
        return

    _, name, new_name = data

    if name == new_name:
        return

    try:
        with open(name, "r") as file_in, open(new_name, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
