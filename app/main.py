def copy_file(command: str) -> None:
    command_list = command.split()
    if command_list[0] == "cp" and len(command_list) == 3:
        if command_list[1] != command_list[2]:
            with (
                open(command_list[1], "r") as input_file,
                open(command_list[2], "w") as output_file
            ):
                source_file_content = input_file.read()
                output_file.write(source_file_content)
