def copy_file(command: str) -> None:
    command_split = command.split(" ")
    if len(command_split) != 3:
        return None
    if command_split[0] != "cp":
        return None
    if command_split[1] == command_split[2]:
        return None
    try:
        existing_file = open(command_split[1], "r")
    except FileNotFoundError:
        return None
    copied_file = open(command_split[2], "w")
    copied_file.write(existing_file.read())
    copied_file.close()
    existing_file.close()
    return None
