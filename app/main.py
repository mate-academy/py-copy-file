def copy_file(command: str) -> None:
    command_ls = command.split()
    if len(command_ls) == 3 and command_ls[0] == "cp":
        old_file_name = command_ls[1]
        new_file_name = command_ls[2]
        if old_file_name != new_file_name:
            try:
                with (open(old_file_name, "r") as file_in,
                      open(new_file_name, "w") as file_out):
                    file_out.write(file_in.read())
            except FileNotFoundError:
                print("No such file to copy")
    else:
        print("Your command is not correct")
