def copy_file(command: str) -> None:
    old_file, new_file = command.split()[1:]
    with open(old_file, "r") as from_file:
        with open(new_file, "w") as to_file:
            to_file.write(from_file.read())
