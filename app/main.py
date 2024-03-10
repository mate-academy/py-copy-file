def copy_file(command: str) -> None:
    command_ls = command.split()
    if command_ls[0] is not "cp":
        raise ValueError

    if command_ls[1] != command_ls[2]:
        with (open(command_ls[1], "r") as file_in,
              open(command_ls[2], "w") as file_out):
            data = file_in.read()
            file_out.write(data)

    else:
        pass
