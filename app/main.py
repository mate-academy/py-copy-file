def copy_file(command: str) -> None:
    command_split = command.split(" ")
    if (len(command_split) == 3
            and command_split[0] == "cp"
            and command_split[1] != command_split[2]):
        with open(command_split[2], "w") as file_in, \
                open(command_split[1], "r") as file_out:
            file_in.writelines(file_out.readlines())
