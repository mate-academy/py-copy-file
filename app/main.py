def copy_file(command: str) -> None:
    if command == "":
        return

    command_list = command.split()
    if len(command_list) != 3:
        return

    if command_list[0] != "cp":
        return

    if command_list[1] == command_list[2]:
        return

    else:
        file_name = command_list[1]
        new_file_name = command_list[2]
        try:
            with (open(file_name, "r") as file_in,
                  open(new_file_name, "w") as file_out):
                for line in file_in:
                    file_out.write(line)
        except FileNotFoundError:
            return
