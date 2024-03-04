def copy_file(command: str) -> None:
    command_text = command.split()
    if command_text[0] != "cp" or command_text[1] == command_text[2]:
        return
    with open(command_text[1], "r") as file_in, \
            open(command_text[2], "w") as file_out:
        file_out.write(str(file_in.readlines()))
