def copy_file(command: str) -> None:
    command_list = command.strip().split()
    if command is None:
        return
    elif len(command_list) != 3:
        return
    elif command_list[0] != "cp":
        return
    elif command_list[1] == command_list[2]:
        return
    else:
        try:
            with (
                open(command_list[1], "r") as old_file,
                open(command_list[2], "w") as new_file
            ):
                old_file_content = old_file.read()
                new_file.write(old_file_content)
        except Exception:
            return
