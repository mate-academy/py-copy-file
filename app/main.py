def copy_file(command: str) -> None:
    if "cp " in command:
        command_ls = command.split()
        if command_ls[1] != command_ls[2]:
            with (
                open(command_ls[1], "r") as source_file,
                open(command_ls[2], "w") as cp_file
            ):
                cp_file.write(source_file.read())
