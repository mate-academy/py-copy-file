def copy_file(command: str) -> None:
    args = command.split()

    print(args)

    if len(args) < 3 or args[0] != "cp":
        return

    if args[1] == args[2]:
        return

    try:
        with open(args[1], "r") as from_file, open(args[2], "w") as to_file:
            content = from_file.read()
            to_file.write(content)
    except FileNotFoundError:
        ...
