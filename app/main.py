def copy_file(command: "str") -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "cp":
        return
    cp, file, new_file = parts
    if file == new_file:
        return
    try:
        with open(file, "r") as file_in, open(new_file, "w") as file_out:
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
