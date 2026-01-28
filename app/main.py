def copy_file(command: str) -> None:
    command_lst = command.split(" ")

    if not (
            len(command_lst) == 3
            and command_lst[0] == "cp"
            and command_lst[1] != command_lst[2]
    ):
        return

    try:
        with (open(command_lst[1], "r") as file_in,
              open(command_lst[2], "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        pass
