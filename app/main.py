def copy_file(command: str) -> None:
    command_list = command.split()
    if len(command_list) == 3 and command_list[0] == "cp":
        source_name, copied_file = command_list[1:]
        if source_name != copied_file:
            with open(
                    source_name, "r"
            ) as source, open(
                copied_file, "w"
            ) as new_file:
                new_file.write(source.read())
