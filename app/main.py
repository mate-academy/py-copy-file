def copy_file(command: str) -> None:
    args = command.split(" ")
    if len(args) != 3 or args[0] != "cp":
        return

    source = args[1]
    destination = args[2]

    if source == destination:
        return

    try:
        with open(source, "rb") as src_file, \
             open(destination, "wb") as dest_file:
            dest_file.write(src_file.read())
    except Exception:
        return
