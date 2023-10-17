def copy_file(command: str) -> None:
    command_list = command.split(" ")
    with (open(command_list[1], "r") as first_file,
          open(command_list[2], "w") as second_file):
        if command_list[0] == command_list[1]:
            return
        second_file.write(first_file.read())
