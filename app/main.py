def copy_file(command: str) -> None:
    command_list = command.split()
    new_file_name = "new_" + command_list[1]
    old_file_name = command_list[2]
    if command_list[0] == "cp" and new_file_name == old_file_name:
        with (open(old_file_name, "r") as file_in,
              open(new_file_name, "w") as file_out):
            file_out.write(file_in.read())
