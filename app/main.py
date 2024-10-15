def copy_file(command: str) -> None:
    command_ls = command.split()
    if (
            len(command_ls) == 3
            and command_ls[0] == "cp"
            and command_ls[1] != command_ls[2]
    ):
        with (
            open(command_ls[1], "r") as r_file,
            open(command_ls[2], "w") as w_file
        ):
            w_file.write(r_file.read())
