def copy_file(command: str) -> None:

    try:
        cp_command, file, copy_of_file = command.split()
    except ValueError:
        return

    if file == copy_of_file or cp_command != "cp":
        return

    with open(file, "r") as source, open(copy_of_file, "w") as copy:
        copy.write(source.read())
