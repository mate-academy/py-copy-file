class CopyFileError(Exception):
    pass


class InvalidCommandError(CopyFileError):
    pass


class SameFileError(CopyFileError):
    pass


class CustomFileNotFoundError(CopyFileError):
    pass


class FileCopyError(CopyFileError):
    pass


def copy_file(copy_command: str) -> None:
    command, source_file, destination_file = copy_command.split()

    if command != "cp" or len(copy_command.split()) != 3:
        raise InvalidCommandError("Invalid command format")
    if source_file == destination_file:
        raise SameFileError(f"{source_file} "
                            f"and {destination_file} files are the same.")
    try:
        with (
            open(source_file, "r") as file_in,
            open(destination_file, "w") as file_out
        ):
            file_out.write(file_in.read())
    except FileNotFoundError:
        raise CustomFileNotFoundError(f"File {source_file} not found.")
    except Exception as e:
        raise FileCopyError(f"An error occurred: {e}")
