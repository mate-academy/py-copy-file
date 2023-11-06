def cope_file(command: str) -> None:
    command_list = command.split(" ")
    if len(command_list) == 3:
        with (open(command_list[1], "r") as old,
              open(command_list[2], "w") as copy):
            copy.write(old.read())
