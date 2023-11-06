def cope_file(command: str) -> None:
    command_list = command.split(" ")
    if (
            len(command_list) == 3
            and command_list[0] == "cp"
            and command_list[1] != command_list[2]
    ):
        with (
            open(command_list[1], "r") as old,
            open(command_list[2], "w") as copy
        ):
            copy.write(old.read())
