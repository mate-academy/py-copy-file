class InvalidCommandFormat(Exception):
    pass


class InvalidCommand(Exception):
    pass


class SameFileError(Exception):
    pass


class SourceFileNotFoundError(Exception):
    pass


class PermissionDeniedError(Exception):
    pass


def copy_file(command: str) -> None:
    commands = command.split()

    if len(commands) != 3:
        raise InvalidCommandFormat("Invalid command format. "
                                   "Usage: cp source_file destination_file")

    command_name, source_file, destination_file = commands

    if command_name != "cp":
        raise InvalidCommand("Invalid command. Use 'cp' to copy files.")

    if source_file == destination_file:
        raise SameFileError("Source file and destination file are the same.")

    try:
        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
    except FileNotFoundError:
        raise SourceFileNotFoundError("Source file not found.")
    except PermissionError:
        raise PermissionDeniedError("Permission denied. Unable to copy file.")
    except Exception as e:
        raise e
