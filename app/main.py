def copy_file(command: str) -> None:
    list_command = command.split()
    if list_command[1] == list_command[2] or list_command[0] != "cp":
        return
    with (open(list_command[1], "r") as file_in,
          open(list_command[2], "w") as file_out):
        file_out.writelines(file_in.read())
