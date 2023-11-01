def copy_file(command: str) -> None:
    command_list = command.split()
    if command_list[1] == command_list[2]:
        pass
    elif command_list[0] == "cp" and len(command_list) == 3:
        with (
            open(command_list[1], "r") as copy,
            open(command_list[2], "w") as paste
        ):
            paste.write(copy.read())
