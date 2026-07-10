def copy_file(command: str) -> None:
    commands_list = command.split(" ")
    if len(commands_list) != 3 or commands_list[0] != "cp":
        return

    if commands_list[1] == commands_list[2]:
        return

    try:
        with (
            open(commands_list[1], "r") as file_in,
            open(commands_list[2], "w") as file_out
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        return
