def copy_file(command: str) -> None:
    command_list = command.split()
    try:
        assert len(command_list) == 3
    except AssertionError:
        return None
    if command_list[0] != "cp" or command_list[1] == command_list[2]:
        return None
    try:
        open(command_list[1], "r"), open(command_list[2], "w")
    except FileNotFoundError:
        return None
    else:
        with (
            open(command_list[1], "r") as source_file,
            open(command_list[2], "w") as copy
        ):
            copy.write(source_file.read())
