import os


class ErrorWithString(Exception):
    pass


class CopyToSelf(Exception):
    pass


class FileNotFound(Exception):
    pass


def copy_file(command: str) -> None:
    try:
        parts = command.split()
        source_file = parts[1]
        destination_file = parts[2]

        if len(parts) != 3 or parts[0] != "cp":
            raise ErrorWithString

        if source_file == destination_file:
            raise CopyToSelf

        if not os.path.isfile(source_file):
            raise FileNotFound

        with (open(source_file, "r") as file_in,
              open(destination_file, "w") as file_out):
            file_out.write(file_in.read())
    except ErrorWithString:
        print("Given string is not executable")
    except CopyToSelf:
        print("Trying to copy file to the same file")
    except FileNotFound:
        print("Not found file in given directory")
