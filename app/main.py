def copy_file(command: str) -> None:
    command_list = command.split(" ")
    if len(command_list) != 3:
        raise ValueError(f"Count of words should be equal 3, "
                         f"got {len(command_list)} instead")
    if command_list[0] != "cp":
        raise NameError(f"No such command {command_list[0]}")
    action, file_name, copy_file_name = command_list
    if file_name != copy_file_name:
        with (open(file_name, "r") as file_in,
              open(copy_file_name, "w") as file_out):
            file_out.write(file_in.read())
