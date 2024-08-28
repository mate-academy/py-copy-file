def copy_file(command: list) -> None:
    parts = command.split()

    if len(parts) != 3 or parts[0] != "cp":
        return

    origin_file, copy_file = parts[1], parts[2]

    if origin_file == copy_file:
        return

    try:
        with open(origin_file, "r") as file_in, \
             open(copy_file, "w") as file_out:
            file_out.write(file_in.read())

    except Exception:
        pass
