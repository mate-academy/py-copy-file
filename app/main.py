def copy_file(command: str) -> None:
    command_list = command.split(" ")

    if command_list[0] == "cp" and command_list[1] != command_list[2]:
        with open(command_list[1], "r") as file_in,\
                open(command_list[2], "w") as file_out:
            copy_text = file_in.read()
            file_out.write(copy_text)
