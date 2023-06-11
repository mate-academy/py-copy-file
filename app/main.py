def copy_file(command: str) -> None:
    command_ls = command.split()
    try:
        with open(command_ls[1], "r") as file_in, open(command_ls[2], "x") as file_out:
            file_out.write(file_in.read())
    except FileExistsError:
        pass
