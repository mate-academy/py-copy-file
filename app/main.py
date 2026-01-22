def copy_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3:
        return

    if command_list[0] == "cp":
        if command_list[1] != command_list[2]:
            try:
                with (
                    open(command_list[1], "r") as file_in,
                    open(command_list[2], "w") as file_out
                ):
                    need_to_write = file_in.read()
                    file_out.write(need_to_write)
            except FileNotFoundError:
                pass
