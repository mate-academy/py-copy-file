def copy_file(command: str) -> str:
    parts_of_command = command.split()
    if parts_of_command[1] == parts_of_command[2]:
        return command

    with open(parts_of_command[1], "r") as copy_from:
        with open(parts_of_command[2], "w") as copy_to:
            copy_to.write(copy_from.read())
