def copy_file(command: str) -> None:
    try:
        curr_command, current_file, new_file = command.split()
    except ValueError:
        return

    if current_file == new_file:
        return

    if curr_command != "cp":
        return

    with open(current_file, "r") as source:
        with open(new_file, "w") as destination:
            destination.write(source.read())


copy_file("cp qwerty.txt new_file.txt")
