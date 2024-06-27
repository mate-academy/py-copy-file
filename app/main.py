def copy_file(command: str) -> None:
    command_list = command.split(" ")
    if len(command_list) != 3 or command_list[1] != "cp":
        raise ValueError(
            "Invalid command. "
            "Command must look like \'cp file.txt file-copy.txt\'"
        )
    if command_list[1] == command_list[2]:
        return None
    with (open(command_list[1], "r") as file_in,
          open(command_list[2], "w") as file_out):
        file_out.write(file_in.read())
