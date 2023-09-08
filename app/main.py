class CustomError(Exception):
    pass


class NameCommandError(CustomError):
    """Command name is not cp"""


class CommandError(CustomError):
    """The error of missing three elements in the team"""


def copy_file(command: str) -> None:
    if command[0] == "cp":
        raise NameCommandError
    command = command.split()

    if len(command) != 3:
        raise CommandError

    if command[1] == command[2]:
        pass

    with open(command[1], "r") as data_file, open(command[2], "w") as new_file:
        data = data_file.read()
        new_file.write(data)
