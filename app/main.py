def copy_file(command: str) -> None:
    if len(command.split()) == 3:
        command_name, file_name, copy_file_name = command.split()
        if file_name != copy_file_name and command_name == "cp":

            with (open(file_name, "r") as file_in,
                  open(copy_file_name, "w") as file_out):
                file_out.write(file_in.read())
