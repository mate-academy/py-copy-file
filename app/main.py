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


def copy_file(command: str) -> None:
    part_command = command.split()

    if len(part_command) != 3 or part_command[0] != "cp":
        raise InvalidCommandError("Invalid command format")

    first_file = part_command[1]
    second_file = part_command[2]

    if first_file == second_file:
        raise SameFileError(f"{first_file} and {second_file} "
                            f"files are the same.")

    try:
        with (
            open(first_file, "r") as file_in,
            open(second_file, "w") as file_out
        ):
            file_out.write(file_in.read())
        print(f"Successfully copied from {first_file} to {second_file}")
    except FileNotFoundError:
        raise CustomFileNotFoundError(f"File {first_file} not found.")
    except Exception as e:
        raise FileCopyError(f"An error occurred: {e}")
