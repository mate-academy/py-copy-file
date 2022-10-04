def copy_file(command: str) -> None:
    list_of_command = command.split()
    if list_of_command[1] == list_of_command[2] or list_of_command[0] != "cp":
        print("Invalid input")
        return
    with (open(list_of_command[1], "r") as file_in,
          open(list_of_command[2], "w") as file_out):
        file_out.writelines(file_in.readlines())
