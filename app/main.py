def copy_file(command: str) -> bool:
    list_command = command.split()
    if len(list_command) == 3 and list_command[0] == "cp":
        if list_command[1] != list_command[2]:
            try:
                with (open(list_command[1], "r") as file_in,
                      open(list_command[2], "w") as file_out):
                    for row in file_in:
                        file_out.write(row)
            except FileNotFoundError:
                return False
