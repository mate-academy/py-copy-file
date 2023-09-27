class NameCommandError(Exception):
    """Command name is not cp"""


class CommandError(Exception):
    """The command must contain exactly 3 elements. Some elements are missing or in excess."""


def copy_file(command: str) -> None:
    command_split = command.split()

    if len(command_split) != 3:
        raise CommandError

    name_command, source_file_name, new_file_name = command_split

    if name_command != "cp":
        raise NameCommandError

    with open(source_file_name) as file, open(new_file_name, "w") as new_file:
        new_file.write(file.read())
