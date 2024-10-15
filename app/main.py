def copy_file(command: str) -> None:
    cmd, origin, dupe = command.split()

    if cmd != "cp" or origin == dupe:
        return
    try:
        with open(origin, "r") as source, open(dupe, "w") as copy:
            copy.write(source.read())
    except FileNotFoundError as e:
        print(f"Error: {e}")
