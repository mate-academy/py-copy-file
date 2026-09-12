def copy_file(command: str) -> None:
    arguments = command.split()
    if len(arguments) != 3 or arguments[0] != "cp":
        return
    old_file = arguments[1]
    new_file = arguments[2]
    if new_file == old_file:
        return
    try:
        with open(old_file, "r") as old_file, open(new_file, "w") as new_file:
            for line in old_file:
                new_file.write(f"{line}")
    except FileNotFoundError:
        pass
