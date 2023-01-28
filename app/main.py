import shutil


class CommandError(Exception):
    pass


def copy_file(command: str) -> None:
    try:
        command, input_file, output_file = command.split(" ")
    except ValueError:
        raise CommandError("Check command arguments")
    if command != "cp":
        raise CommandError("Check input command")
    shutil.copyfile(input_file, output_file)
