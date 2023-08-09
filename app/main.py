def copy_file(command: str) -> None:
    command_in_list = command.split(" ")
    if command_in_list[0] == "cp" and command_in_list[1] != command_in_list[2]:
        with (open(command_in_list[1], "r") as file_in,
              open(command_in_list[2], "w") as file_out):
            file_out.write(file_in.read())
