class InvalidCommandError(Exception):
    pass


def copy_file(command: str) -> None:
    command_attributes = command.split()
    if command_attributes[0] != "cp":
        raise InvalidCommandError

    with open(command_attributes[1], "r") as file_in,\
         open(command_attributes[2], "w") as file_out:
        if file_in == file_out:
            return
        file_out.write(file_in.read())
