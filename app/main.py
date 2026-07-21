def copy_file(command: str) -> None:
    command_list = command.split()

    if len(command_list) != 3 or command_list[0] != "cp":
        return

    source_file_name = command_list[1]
    new_file_name = command_list[2]

    if source_file_name == new_file_name:
        return

    try:
        with open(source_file_name, "r") as source_file, open(
            new_file_name, "w"
        ) as new_file:
            new_file.write(source_file.read())
    except FileNotFoundError:
        return
