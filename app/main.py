def copy_file(command: str) -> None:
    command_ls = command.split()

    if len(command_ls) == 3 and command_ls[0] == "cp":
        file_1 = command_ls[1]
        file_2 = command_ls[2]
    else:
        return

    if file_1 != file_2:
        try:
            with open(file_1, "r") as f:
                content = f.read()
            with open(file_2, "w") as newf:
                newf.write(content)
        except FileNotFoundError:
            pass
