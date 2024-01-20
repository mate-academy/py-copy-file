class CopyFileError(Exception):
    pass


def copy_file(command: str) -> None:
    command_split = command.split()
    if len(command_split) != 3:
        raise CopyFileError("Invalid command input")

    instruction, f_in_name, f_out_name = command_split
    if instruction != "cp" or f_in_name == f_out_name:
        raise CopyFileError("Invalid command or file name")

    with open(f_in_name, "r") as file_in, open(f_out_name, "w") as file_out:
        file_out.write(file_in.read())
