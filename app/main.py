def copy_file(command: str) -> None:
    if len(command) > 0:
        command_name, file_in_name, file_out_name = command.split()
        if file_in_name == file_out_name or command_name != "cp":
            exit()
        with (open(file_in_name, "r") as file_in,
              open(file_out_name, "w") as file_out):
            file_out.write(file_in.read())
