def copy_file(command: str) -> None:
    full_command = command.split(" ")
    if not len(full_command) == 3:
        return
    command, filename_to_copy, filename_target = full_command
    if command != "cp":
        return
    if filename_to_copy == filename_target:
        return
    try:
        with open(filename_to_copy, "r") as file_to_copy, open(
            filename_target, "w"
        ) as file_to_write:
            content = file_to_copy.read()
            file_to_write.write(content)
    except FileNotFoundError:
        return
