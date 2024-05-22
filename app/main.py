def copy_file(command: str) -> None:
    command_ls = command.split()
    if len(command_ls) == 3:
        prefix = command.split()[0]
        file_name = command.split()[1]
        copy_file_name = command.split()[2]
        if prefix == "cp" and file_name != copy_file_name:
            with (
                open(file_name, "r") as file_in,
                open(copy_file_name, "w") as file_out
            ):
                file_out.write(file_in.read())
