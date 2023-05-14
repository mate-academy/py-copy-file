def copy_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3 or command_split[0] != "cp":
        return print("Wrong command!")
    file_in_name = command_split[1]
    file_out_name = command_split[2]
    if file_out_name == file_out_name:
        return
    with (open(f"{file_in_name}", "r") as file_in,
          open(f"{file_out_name}", "w") as file_out):
        file_out.write(file_in.read())
