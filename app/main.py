def copy_file(command: str) -> None:
    parts_of_command = command.split()
    if len(parts_of_command) != 3 or parts_of_command[0] != "cp":
        return

    file, copy_of_file = parts_of_command[1], parts_of_command[2]
    if file == copy_of_file:
        return

    with open(file, "r") as source, open(copy_of_file, "w") as copy:
        copy.write(source.read())
