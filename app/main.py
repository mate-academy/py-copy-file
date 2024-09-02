from errors import (InvalidCommandError,
                    InvalidFileError,
                    InvalidFileCountError,
                    InvalidPathError)


def copy_file(command: str) -> int:
    args_list = command.split()
    if len(args_list) != 3:
        raise InvalidFileCountError("Invalid file count")
    elif args_list[0] != "cp":
        raise InvalidCommandError("Invalid command")
    elif args_list[1] == args_list[2]:
        raise InvalidFileError("Invalid file")
    elif ("/" in args_list[1]) or ("/" in args_list[2]):
        raise InvalidPathError("Invalid path")
    else:
        try:
            with (open(args_list[1], "r") as read_file,
                 open(args_list[2], "a") as write_file):
                for line in read_file:
                    write_file.write(line)
        except FileNotFoundError:
            raise
        else:
            return 0
