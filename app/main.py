def copy_file(command: str) -> None:
    args = command.split()

    if len(args) != 3 or args[0] != "cp" or args[1] == args[2]:
        return

    file_in = args[1]
    file_out = args[2]
    try:
        with open(file_in, "r") as from_file, open(file_out, "w") as to_file:
            content = from_file.read()
            to_file.write(content)
    except FileNotFoundError:
        ...
