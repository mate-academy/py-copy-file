def copy_file(command: str) -> None:
    command_list = command.split()
    if (isinstance(command, str)) and len(command_list) == 3:
        command, file_in, file_out = command_list
        if command == "cp" and file_in != file_out:
            with (open(file_in, "r") as file_in,
                  open(file_out, "w") as file_out):
                file_out.write(file_in.read())
