def copy_file(command: str) -> None:
    command_list = command.split()
    copy_command = command_list[0]
    file_in_name = command_list[1]
    file_out_name = command_list[2]
    if file_in_name != file_out_name and copy_command == "cp":
        with (open(file_in_name, "r") as file_in,
              open(file_out_name, "w") as file_out):
            file_out.write(file_in.read())
