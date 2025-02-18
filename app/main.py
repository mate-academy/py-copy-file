from typing import Tuple


class CommandNameError(Exception):
    def __str__(self) -> str:
        return ("Wrong command name! correct format is:"
                " cp <source_name.txt> <copy_name.txt>")


class FileNameError(Exception):
    def __str__(self) -> str:
        return ("Source and copy paths are the same. "
                "Please provide different paths.")


def validate_command(command_string: str) -> Tuple:
    try:
        prefix, source_path, copy_path = command_string.split()
    except (ValueError, AttributeError):
        raise CommandNameError
    if prefix != "cp":
        raise CommandNameError
    if source_path == copy_path:
        raise FileNameError
    return source_path, copy_path


def copy_file(command: str) -> None:

    source_path, copy_path = validate_command(command)
    with open(source_path, "r") as source, open(copy_path, "w") as copy:
        source_content = source.read()
        copy.write(source_content)
