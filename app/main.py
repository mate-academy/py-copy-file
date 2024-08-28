def copy_file(command: str) -> None:
    command_list = command.split(" ")[1:]

    if command_list[0] == command_list[1]:
        pass
    else:
        with (open(command_list[0], "r") as file_in,
              open(command_list[1], "w") as file_out):
            file_out.write(file_in.read())
