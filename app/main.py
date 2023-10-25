def copy_file(command: str) -> None:
    args = command.split()

    if len(args) != 3 or args[1] == args[2]:
        return

    cp, path, new_path = args

    try:
        with open(path, "r") as file_in, open(new_path, "w") as file_out:
            file_out.write(file_in.read())

    except FileNotFoundError:
        print(print(f"File: {path} not found."))
