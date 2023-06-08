from shutil import copy
from os.path import exists


def copy_file(command: str) -> None:
    try:
        cmd, source, destination = command.split()
        if cmd != "cp":
            raise ValueError("Unknown command")
        if source == destination:
            raise ValueError("Destination must differ from the source")
        if not exists(source):
            raise FileNotFoundError(f"Unable to find the "
                                    f"source file at '{source}'")
        copy(source, destination)
    except (ValueError, FileNotFoundError) as er:
        print(f"Error: {er}")
    except Exception as er:
        print(f"Unexpected error: {er}")
