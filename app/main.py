from shutil import copy
from os.path import exists


class ArgumentException(Exception):
    pass


def copy_file(command: str) -> None:
    try:
        cmd, source, destination = command.split()
        if cmd != "cp":
            raise ArgumentException("Unknown command")
        if source == destination:
            raise ArgumentException("Destination must differ from the source")
        if not exists(source):
            raise FileNotFoundError(f"Unable to find the "
                                    f"source file at '{source}'")
    except ValueError:
        print("You have to provide 3 parameters in the command string")
    except ArgumentException as er:
        print(f"Invalid arguments: {er}")
    except FileNotFoundError as er:
        print(er)
    except Exception as er:
        print(f"Unexpected error: {er}")
    else:
        copy(source, destination)
