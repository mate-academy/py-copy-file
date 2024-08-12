def copy_file(command: str) -> None:
    command_content = command.split()
    if len(command_content) == 3:
        if command_content[0] == "cp":
            if command_content[1] != command_content[2]:
                with (open(command_content[1], "r") as file_in,
                      open(command_content[2], "w") as file_out):
                    file_out.write(file_in.read())
