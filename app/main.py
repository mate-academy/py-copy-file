def copy_file(command: str) -> None:

    command = command.split(" ")

    if len(command) != 3 or command[0] != "cp":
        return

    source = command[1]
    dest = command[2]

    if source == dest:
        return

    try:
        with open(source, "r") as src_file, open(dest, "w") as dest_file:
            dest_file.write(src_file.read())
    except FileNotFoundError:
        return
