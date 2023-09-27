class NameCommandError(Exception):
    """Command name is not cp"""


class CommandError(Exception):
    """The error of missing three elements in the team"""


def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        raise CommandError

    name_command, source_file_name, new_file_name = command.split()

    if name_command != "cp":
        raise NameCommandError

    with open(source_file_name) as file, open(new_file_name, "w") as new_file:
        new_file.write(file.read())
