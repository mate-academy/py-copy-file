def copy_file(command: str) -> None:
    cmd_list = command.split()
    if len(cmd_list) != 3 or cmd_list[1] == cmd_list[2]:
        return
    if cmd_list[0] == "cp":
        try:
            with (
                open(cmd_list[1], "r") as file,
                open(cmd_list[2], "w") as new_file
            ):
                new_file.write(file.read())
                file.close()
                new_file.close()
        except FileNotFoundError:
            return
