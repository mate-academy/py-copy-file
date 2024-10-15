from shutil import copy


def copy_file(command: str) -> None:
    _, source_file, destination_file = command.split(" ")

    if source_file == destination_file:
        return

    copy(source_file, destination_file)
