class CopyCommandError(Exception):
    pass


class InvalidCommandError(CopyCommandError):
    pass


class SameFileError(CopyCommandError):
    pass


def copy_file(command: str) -> None:
    file_names = command.split()
    if len(file_names) != 3 or file_names[0] != "cp":
        raise InvalidCommandError("The command is incorrect!")
    if file_names[1] == file_names[2]:
        raise SameFileError("It is the same file!")
    with (open(file_names[1], "r") as file_in,
          open(file_names[2], "w") as file_out):
        file_out.write(file_in.read())
