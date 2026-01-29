def copy_file(command: str) -> None:
    command_split = command.split()
    if len(command) == 0:
        return
    if len(command_split) < 3:
        return
    if command_split[0] != "cp":
        return

    file_name = command_split[1]
    new_file_name = command_split[2]

    if file_name == new_file_name:
        return
    source_content = ""

    try:
        with open(file_name, "r") as source_file:
            source_content = source_file.read()
    except Exception:
        pass
    else:
        with open(new_file_name, "w") as new_file:
            new_file.write(source_content)
