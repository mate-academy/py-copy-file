import shutil


class CommandTypeError(Exception):
    pass


def copy_file(command: str) -> None:
    command, input_file, output_file = command.split(" ")
    if command != "cp":
        raise CommandTypeError("Check input command")
    shutil.copyfile(input_file, output_file)
