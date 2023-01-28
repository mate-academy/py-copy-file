import shutil


def copy_file(command: str) -> None:
    command, input_file, output_file = command.split(" ")
    shutil.copyfile(input_file, output_file)
