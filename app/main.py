def copy_file(command: str) -> None:
    part = command.split()
    command_cp = part[0]
    if command_cp != "cp":
        return
    if len(part) != 3:
        print("Error: The command requires exactly 3 arguments.")
        return

    file_copy_from = part[1]
    file_copy_to = part[2]
    if file_copy_to == file_copy_from:
        return
    with open(file_copy_from, "r") as source:
        with open(file_copy_to, "w") as destination:
            destination.write(source.read())
