def copy_file(command: str) -> None | str:
    command_list = command.split()
    if len(command_list) != 3:
        return "string should include 3 parameters"
    if command_list[0] != "cp":
        return "This command doesn't exist"
    if command_list[1] == command_list[2]:
        return None
    else:
        with (open(command_list[1], "r") as file_in,
              open(command_list[2], "w") as file_out):
            copy = file_in.read()
            file_out.write(str(copy))
