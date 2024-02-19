def copy_file(command: str) -> None | str:
    command_list = command.split()

    if command_list[0] != "cp":
        return (
            f"Wrong command has been entered '{command_list[0]}'"
            f" (only the 'cp' command is accepted)"
        )

    if command_list[1] == command_list[2]:
        return

    with (open(command_list[1], "r") as original,
          open(command_list[2], "w") as copy):
        copy.write(original.read())
