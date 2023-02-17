import re


class IncorrectCommand(Exception):
    """Error if command has incorrect format"""


def copy_file(command: str) -> None:
    command_format = r"cp \w+.txt \w+.txt"
    if not re.match(command_format, command):
        raise IncorrectCommand(f"{command} has incorrect format")
    copied_file, new_file = command.split()[1], command.split()[2]
    if copied_file != new_file:
        with open(copied_file, "r") as old, open(new_file, "w") as new:
            new.write(old.read())
