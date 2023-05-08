def copy_file(command: str) -> None:
    command_list = command.split()
    source_name = command_list[1]
    copied_file = command_list[2]
    if len(command_list) == 3:
        if source_name != copied_file:
            with open(
                    source_name, "r"
            ) as source, open(
                    copied_file, "w"
            ) as new_file:
                for line in source:
                    new_file.write(line)
