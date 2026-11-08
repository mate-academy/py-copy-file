def copy_file(command: str) -> None:
    command_split = command.split(" ")
    if len(command_split) != 3:
        return None
    if command_split[0] != "cp":
        return None
    if command_split[1] == command_split[2]:
        return None
    try:
        with (open(command_split[1], "r") as existing_file,
              open(command_split[2], "w") as copied_file):
            copied_file.write(existing_file.read())
    except FileNotFoundError:
        return None
    return None
