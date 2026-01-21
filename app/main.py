def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) != 3:
        print("length your command must be 3")
        return None
    command, file_name_input, file_name_output = command_list
    if command == "cp" and file_name_input != file_name_output:
        with (open(file_name_input, "r") as file_in,
              open(file_name_output, "w") as file_out):
            file_out.write(file_in.read())
