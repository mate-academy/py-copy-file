def copy_file(command: str) -> None:
    if "cp " in command:
        command_ls = command.split()
        source_file_name = command_ls[1]
        cp_file_name = command_ls[2]
        if source_file_name != cp_file_name:
            with (
                open(source_file_name, "r") as source_file,
                open(cp_file_name, "w") as cp_file
            ):
                cp_file.write(source_file.read())
