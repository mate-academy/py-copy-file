def copy_file(command: str) -> None:

    command_user = command.split(" ")

    if len(command_user) < 3:
        raise ValueError("Command must have at least 3 arguments")

    if command_user[0] != "cp":
        raise ValueError("Command must start with 'cp' to copy files")

    file_src = command_user[1]
    file_copy = command_user[2]

    if not file_src == file_copy:
        with open(file_src, "r") as file_in, open(file_copy, "w") as file_out:
            file_out.write(file_in.read())
