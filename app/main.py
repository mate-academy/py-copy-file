def copy_file(command: str) -> None:
    command_listed = command.split(" ")
    if command_listed[1] == command_listed[2]:
        return
    with open(command_listed[1], "r") as file_in, \
            open(command_listed[2], "w") as file_out:
        file_out.write(file_in.read())
